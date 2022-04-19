#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 11:49:01 2022

@author: mlampert
"""

import os
import copy
import pickle


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import MaxNLocator

from flap_nstx.gpi import calculate_nstx_gpi_frame_by_frame_velocity
from flap_nstx.gpi import show_nstx_gpi_video_frames
from flap_nstx.gpi import calculate_nstx_gpi_angular_velocity
from flap_nstx.gpi import plot_nstx_gpi_angular_velocity_distribution, plot_nstx_gpi_velocity_distribution
from flap_nstx.analysis import plot_angular_vs_translational_velocity

import flap
import flap_nstx
wd=flap.config.get_all_section('Module NSTX_GPI')['Working directory']
fig_dir='/publication_figures/pop_2022'

    
thisdir = os.path.dirname(os.path.realpath(__file__))
fn = os.path.join(thisdir,"../flap_nstx.cfg")
flap.config.read(file_name=fn)
flap_nstx.register()
styled=True

if styled:
    plt.rc('font', family='serif', serif='Helvetica')
    labelsize=8.
    linewidth=0.5
    major_ticksize=2.
    plt.rc('text', usetex=False)
    plt.rcParams['pdf.fonttype'] = 42
    plt.rcParams['ps.fonttype'] = 42
    plt.rcParams['lines.linewidth'] = linewidth
    plt.rcParams['axes.linewidth'] = linewidth
    plt.rcParams['axes.labelsize'] = labelsize
    plt.rcParams['axes.titlesize'] = labelsize
    
    plt.rcParams['xtick.labelsize'] = labelsize
    plt.rcParams['xtick.major.size'] = major_ticksize
    plt.rcParams['xtick.major.width'] = linewidth
    plt.rcParams['xtick.minor.width'] = linewidth/2
    plt.rcParams['xtick.minor.size'] = major_ticksize/2
    
    plt.rcParams['ytick.labelsize'] = labelsize
    plt.rcParams['ytick.major.width'] = linewidth
    plt.rcParams['ytick.major.size'] = major_ticksize
    plt.rcParams['ytick.minor.width'] = linewidth/2
    plt.rcParams['ytick.minor.size'] = major_ticksize/2
    plt.rcParams['legend.fontsize'] = labelsize
else:
    import matplotlib.style as pltstyle
    pltstyle.use('default')

class NoobError(Exception):
    pass

def plot_results_for_pop_2022(plot_figure=2,
                              plot_all=False,
                              save_data_into_txt=False,
                              gaussian_blur=True,
                              subtraction_order=2,
                              flap_or_skim='flap'):
    
    if plot_all:
        plot_figure=-1
        for i in range(12):
            plot_results_for_pop_2022(plot_figure=i,
                                      save_data_into_txt=save_data_into_txt)
    
    
    """
    ELM figure
    """
    if plot_figure == 1:
        print('This is the ELM figure, no need for calculation.')
        
    """
    GPI figure
    """  
    if plot_figure == 2:
        print('This is the GPI figure, no need for calculation.')
        
    """
    Example frame pairs with observable rotation in between them
    """
    
    if plot_figure == 3:     
        result=calculate_nstx_gpi_angular_velocity(exp_id=141319,
                                                   time_range=[0.5524,0.5526],  
                                                   normalize='roundtrip', 
                                                   normalize_for_velocity=True, 
                                                   plot=False, 
                                                   pdf=True,
                                                   nocalc=False,
                                                   plot_scatter=False,
                                                   plot_for_publication=True,
                                                   gaussian_blur=gaussian_blur,
                                                   calculate_half_fft=False,
                                                   test_into_pdf=True,
                                                   return_results=True,
                                                   
                                                   subtraction_order_for_velocity=subtraction_order,
                                                   sample_to_plot=[20873,20874],
                                                   save_data_for_publication=True,
                                                   data_filename=wd+fig_dir+'/data_accessibility/fig_34')

    if plot_figure == 4:
        result=calculate_nstx_gpi_angular_velocity(exp_id=141319,
                                                   time_range=[0.5524,0.5526],  
                                                   normalize='roundtrip', 
                                                   normalize_for_velocity=True, 
                                                   plot=False, 
                                                   pdf=True,
                                                   nocalc=False,
                                                   plot_scatter=False,
                                                   plot_for_publication=False,
                                                   gaussian_blur=gaussian_blur,
                                                   calculate_half_fft=False,
                                                   test_into_pdf=False,
                                                   return_results=True,
                                                   plot_ccf=True,
                                                   subtraction_order_for_velocity=subtraction_order,
                                                   sample_to_plot=[20874],
                                                   save_data_for_publication=True,
                                                   data_filename=wd+fig_dir+'/data_accessibility/fig_34')
    """
    Flowchart of the Fourier Mellin based method
    """
    if plot_figure == 5:
        print('This is the flowchart figure, no need to plot.')
        
        
    """
    Example set of subsequent frames clearly exhibiting rotation
    """
    if plot_figure == 6:
        plt.figure()
        ax,fig=plt.subplots(figsize=(3.35*2,5.5))
        pdf=PdfPages(wd+fig_dir+'/fig_1413190.552500_9_frame.pdf')
        show_nstx_gpi_video_frames(exp_id=141319, 
                                   start_time=0.552500-6*2.5e-6,
                                   n_frame=9,
                                   logz=False,
                                   z_range=[0,3900],
                                   plot_filtered=False, 
                                   normalize=False,
                                   cache_data=False, 
                                   plot_flux=False, 
                                   plot_separatrix=True, 
                                   flux_coordinates=False,
                                   device_coordinates=True,
                                   new_plot=False,
                                   save_pdf=True,
                                   colormap='gist_ncar',
                                   save_for_paraview=False,
                                   colorbar_visibility=False,
                                   save_data_for_publication=True,
                                   data_filename=wd+fig_dir+'/data_accessibility/fig_1413190.552500_9_frame.txt'
                                   )
        pdf.savefig()
        pdf.close()
    
    """
    Filament rotation estimation for the single shot
    """
    if plot_figure == 7:
        
        plt.rc('font', family='serif', serif='Helvetica')
        labelsize=7.
        linewidth=0.4
        major_ticksize=2.
        plt.rc('text', usetex=False)
        plt.rcParams['pdf.fonttype'] = 42
        plt.rcParams['ps.fonttype'] = 42
        plt.rcParams['lines.linewidth'] = linewidth
        plt.rcParams['axes.linewidth'] = linewidth
        plt.rcParams['axes.labelsize'] = labelsize
        plt.rcParams['axes.titlesize'] = labelsize
        
        plt.rcParams['xtick.labelsize'] = labelsize
        plt.rcParams['xtick.major.size'] = major_ticksize
        plt.rcParams['xtick.major.width'] = linewidth
        plt.rcParams['xtick.minor.width'] = linewidth/2
        plt.rcParams['xtick.minor.size'] = major_ticksize/2
        
        plt.rcParams['ytick.labelsize'] = labelsize
        plt.rcParams['ytick.major.width'] = linewidth
        plt.rcParams['ytick.major.size'] = major_ticksize
        plt.rcParams['ytick.minor.width'] = linewidth/2
        plt.rcParams['ytick.minor.size'] = major_ticksize/2
        plt.rcParams['legend.fontsize'] = labelsize

        result=calculate_nstx_gpi_angular_velocity(exp_id=141319,
                                                   time_range=[0.552,0.553],  
                                                   normalize='roundtrip', 
                                                   normalize_for_velocity=True, 
                                                   plot=False, 
                                                   pdf=True,
                                                   nocalc=True,
                                                   plot_scatter=False,
                                                   plot_for_publication=True,
                                                   
                                                   return_results=True,
                                                   subtraction_order_for_velocity=2,
                                                   gaussian_blur=True,
                                                   )
        if save_data_into_txt:
            filename=wd+fig_dir+'/data_accessibility/figure_7abcd.txt'
            file1=open(filename, 'w+')
            time=result['Time']
            radial_velocity=result['Velocity ccf FLAP'][:,0]
            poloidal_velocity=result['Velocity ccf FLAP'][:,1]
            angular_velocity=result['Angular velocity ccf FLAP']
            expansion_velocity=result['Expansion velocity ccf FLAP']
            
            file1.write('#Time (ms)\n')
            for i in range(1, len(time)):
                file1.write(str(time[i])+'\t')
                
            file1.write('\n#Radial velocity (m/s)\n')
            for i in range(1, len(radial_velocity)):
                file1.write(str(radial_velocity[i])+'\t')
                
            file1.write('\n#Poloidal velocity (m/s)\n')
            for i in range(1, len(poloidal_velocity)):
                file1.write(str(poloidal_velocity[i])+'\t')
                
            file1.write('\n#Angular velocity (rad/s)\n')
            for i in range(1, len(angular_velocity)):
                file1.write(str(angular_velocity[i])+'\t')                
                
            file1.write('\n#Expansion velocity (1/s)\n')
            for i in range(1, len(expansion_velocity)):
                file1.write(str(expansion_velocity[i])+'\t')                      
            file1.close()    

    """
    Evolution of the rotation and expansion distribution functions
    """
    if plot_figure == 8:
        time_vec, y_vector = plot_nstx_gpi_angular_velocity_distribution(plot_for_publication=True,
                                                                         window_average=500e-6,
                                                                         subtraction_order=subtraction_order,
                                                                         correlation_threshold=0.6,
                                                                         pdf=False,
                                                                         plot=False,
                                                                         return_results=True,
                                                                         plot_all_time_traces=False,
                                                                         tau_range=[-1e-3,1e-3])
        figsize=(8.5/2.54,8.5/np.sqrt(2)/2.54)
        plt.rc('font', family='serif', serif='Helvetica')
        labelsize=8
        linewidth=0.4
        major_ticksize=2
        plt.rc('text', usetex=False)
        plt.rcParams['pdf.fonttype'] = 42
        plt.rcParams['ps.fonttype'] = 42
        
        plt.rcParams['lines.linewidth'] = linewidth
        plt.rcParams['axes.linewidth'] = linewidth
        plt.rcParams['axes.labelsize'] = labelsize
        plt.rcParams['axes.titlesize'] = labelsize
        
        plt.rcParams['xtick.labelsize'] = labelsize
        plt.rcParams['xtick.major.size'] = major_ticksize
        plt.rcParams['xtick.major.width'] = linewidth
        plt.rcParams['xtick.minor.width'] = linewidth/2
        plt.rcParams['xtick.minor.size'] = major_ticksize/2
        
        plt.rcParams['ytick.labelsize'] = labelsize
        plt.rcParams['ytick.major.width'] = linewidth
        plt.rcParams['ytick.major.size'] = major_ticksize
        plt.rcParams['ytick.minor.width'] = linewidth/2
        plt.rcParams['ytick.minor.size'] = major_ticksize/2
        plt.rcParams['legend.fontsize'] = labelsize
        
        pdf_object=PdfPages(wd+fig_dir+'/fig_ang_velocity_distribution_log.pdf')
            

        import matplotlib
        matplotlib.use('agg')
            
        def fmt(x, pos):
            a = '{:3.2f}'.format(x)
            return a
        
        plt.figure()
        fig,((ax1,ax2),(ax3,ax4))=plt.subplots(2,2,figsize=figsize)
        for key in ['Angular velocity ccf '+flap_or_skim+' log',
                    'Expansion velocity ccf '+flap_or_skim+'']:
            
            if key == 'Angular velocity ccf '+flap_or_skim+' log':
                ax=ax1
                corner_text='(a)'
            else:
                ax=ax3
                corner_text='(c)'
            im=ax.contourf(time_vec*1e3,
                           y_vector[key]['bins'],
                           y_vector[key]['data'].transpose(),
                           levels=50,
                           )
            ax.plot(time_vec*1e3,
                     y_vector[key]['median'],
                     color='red',
                     lw=linewidth)
            ax.plot(time_vec*1e3,
                     y_vector[key]['10th'],
                     color='white',
                     lw=linewidth/2)
            ax.plot(time_vec*1e3,
                     y_vector[key]['90th'],
                     color='white',
                     lw=linewidth/2)
            ax.text(-0.5, 1.2, corner_text, transform=ax.transAxes, size=9)
            ax.set_title('Relative frequency of '+y_vector[key]['ylabel'])
            ax.set_xlabel('$t-t_{ELM}$ [$\mu$s]')
            ax.set_ylabel(y_vector[key]['ylabel']+' ['+y_vector[key]['unit']+']')
            ax.xaxis.set_major_locator(MaxNLocator(5)) 
            ax.yaxis.set_major_locator(MaxNLocator(5))
            ax.set_ylim(np.min(y_vector[key]['10th']),
                        np.max(y_vector[key]['90th']))
            ax.set_xticks(ticks=[-500,-250,0,250,500])
            
            import matplotlib.ticker as ticker
            cbar=fig.colorbar(im, format=ticker.FuncFormatter(fmt), ax=ax)
            cbar.ax.tick_params(labelsize=6)

            if key == 'Angular velocity ccf '+flap_or_skim+' log':
                ax=ax2
                corner_text='(b)'
            else:
                ax=ax4
                corner_text='(d)'
            # nwin=y_vector[key]['Data'].shape[0]//2
    #        plt.plot(y_vector[key]['Bins'], np.mean(y_vector[key]['Data'][nwin-2:nwin+3,:], axis=0))
            ax.plot(time_vec*1e3,
                     y_vector[key]['median'],
                     color='red',
                     lw=linewidth)
            
            ax.set_title('Median '+y_vector[key]['ylabel']+' evolution')
            ax.set_xlabel('$t-t_{ELM}$ [$\mu$s]')
            ax.set_ylabel(y_vector[key]['ylabel']+' ['+y_vector[key]['unit']+']')
            ax.set_xlim([-500,500])
            # ax.xaxis.set_major_locator(MaxNLocator(5)) 
            ax.yaxis.set_major_locator(MaxNLocator(5)) 
            ax.xaxis.set_major_locator(MaxNLocator(5)) 
            ax.set_xticks(ticks=[-500,-250,0,250,500])
            ax.text(-0.5, 1.2, corner_text, transform=ax.transAxes, size=9)
        plt.tight_layout(pad=0.1)
        pdf_object.savefig()
        pdf_object.close()
        matplotlib.use('qt5agg')
            
        if save_data_into_txt:
            for ind in [5,7]:
                if ind == 5:
                    filename=wd+fig_dir+'/data_accessibility/figure_8ab.txt'
                if ind == 7:
                    filename=wd+fig_dir+'/data_accessibility/figure_8cd.txt'
                    
                file1=open(filename, 'w+')

                file1.write('#Time (ms)\n')
                for i in range(1, len(time_vec)):
                    file1.write(str(time_vec[i])+'\t')
                    
                file1.write('\n#Median\n')
                for i in range(1, len(y_vector[key]['median'])):
                    file1.write(str(y_vector[key]['median'])+'\t')
                    
                file1.write('\n#10th perc.\n')
                for i in range(1, len(y_vector[key]['10th'])):
                    file1.write(str(y_vector[key]['10th'])+'\t')
                    
                file1.write('\n#90th perc.\n')
                for i in range(1, len(y_vector[key]['90th'])):
                    file1.write(str(y_vector[key]['90th'])+'\t')    
                    
                file1.write('\n#Distribution bins\n')
                for i in range(1, len(y_vector[key]['bins'])):
                    file1.write(str(y_vector[key]['bins'])+'\t')
                file1.write('\n#Distribution\n')
                
                for i in range(len(y_vector[key]['data'][0,:])):
                    string=''
                    for j in range(len(y_vector[key]['data'][:,0])):
                        string+=str(y_vector[key]['data'][j,i])+'\t'
                    string+='\n'
                    file1.write(string)   
                file1.close()
            
    """
    vrad,r-r_sep distribution plotting
    """
    
    if plot_figure == 9:
        time_vec, y_vector = plot_nstx_gpi_velocity_distribution(plot_for_publication=False,
                                                                 pdf=False,
                                                                 plot=False,
                                                                 return_results=True,
                                                                 figure_size=4.25)
        figsize=(8.5/2.54,8.5/np.sqrt(2)/2.54)
        plt.rc('font', family='serif', serif='Helvetica')
        labelsize=8
        linewidth=0.4
        major_ticksize=2
        plt.rc('text', usetex=False)
        plt.rcParams['pdf.fonttype'] = 42
        plt.rcParams['ps.fonttype'] = 42
        
        plt.rcParams['lines.linewidth'] = linewidth
        plt.rcParams['axes.linewidth'] = linewidth
        plt.rcParams['axes.labelsize'] = labelsize
        plt.rcParams['axes.titlesize'] = labelsize
        
        plt.rcParams['xtick.labelsize'] = labelsize
        plt.rcParams['xtick.major.size'] = major_ticksize
        plt.rcParams['xtick.major.width'] = linewidth
        plt.rcParams['xtick.minor.width'] = linewidth/2
        plt.rcParams['xtick.minor.size'] = major_ticksize/2
        
        plt.rcParams['ytick.labelsize'] = labelsize
        plt.rcParams['ytick.major.width'] = linewidth
        plt.rcParams['ytick.major.size'] = major_ticksize
        plt.rcParams['ytick.minor.width'] = linewidth/2
        plt.rcParams['ytick.minor.size'] = major_ticksize/2
        plt.rcParams['legend.fontsize'] = labelsize
        
        pdf_object=PdfPages(wd+fig_dir+'/fig_trans_velocity_distribution.pdf')
            

        import matplotlib
        matplotlib.use('agg')
            
        def fmt(x, pos):
            a = '{:3.2f}'.format(x)
            return a
        plt.figure()
        fig,((ax1,ax2),(ax3,ax4))=plt.subplots(2,2,figsize=figsize)
        for key in ['Velocity ccf radial','Distance']:
            if key == 'Velocity ccf radial':
                ax=ax1
                corner_text='(a)'
            else:
                ax=ax3
                corner_text='(c)'
            im=ax.contourf(time_vec*1e3,
                           y_vector[key]['bins'],
                           y_vector[key]['data'].transpose(),
                           levels=50,
                           )
            ax.plot(time_vec*1e3,
                     y_vector[key]['median'],
                     color='red',
                     lw=linewidth)
            ax.plot(time_vec*1e3,
                     y_vector[key]['10th'],
                     color='white',
                     lw=linewidth/2)
            ax.plot(time_vec*1e3,
                     y_vector[key]['90th'],
                     color='white',
                     lw=linewidth/2)
            
            ax.set_title('Relative frequency of '+y_vector[key]['ylabel'])
            ax.set_xlabel('$t-t_{ELM}$ [$\mu$s]')
            ax.set_ylabel(y_vector[key]['ylabel']+' ['+y_vector[key]['unit']+']')
            ax.set_ylim(np.min(y_vector[key]['10th']),
                        np.max(y_vector[key]['90th']))
            ax.xaxis.set_major_locator(MaxNLocator(5)) 
            ax.yaxis.set_major_locator(MaxNLocator(5))
            ax.set_xticks(ticks=[-500,-250,0,250,500])
            ax.text(-0.5, 1.2, corner_text, transform=ax.transAxes, size=9)
            import matplotlib.ticker as ticker
            cbar=fig.colorbar(im, format=ticker.FuncFormatter(fmt), ax=ax)
            cbar.ax.tick_params(labelsize=6)
            
    
        for key in ['Velocity ccf radial','Distance']:
            if key == 'Velocity ccf radial':
                ax=ax2
                corner_text='(b)'
            else:
                ax=ax4
                corner_text='(d)'
            # nwin=y_vector[i]['Data'].shape[0]//2
    #        plt.plot(y_vector[i]['Bins'], np.mean(y_vector[i]['Data'][nwin-2:nwin+3,:], axis=0))
            ax.plot(time_vec*1e3,
                     y_vector[key]['median'],
                     color='red',
                     lw=linewidth)
            
            ax.set_title('Median '+y_vector[key]['ylabel']+' evolution')
            ax.set_xlabel('$t-t_{ELM}$ [$\mu$s]')
            ax.set_ylabel(y_vector[key]['ylabel']+' ['+y_vector[key]['unit']+']')
            ax.set_xlim([-500,500])
            ax.xaxis.set_major_locator(MaxNLocator(5)) 
            ax.set_xticks(ticks=[-500,-250,0,250,500])
            ax.yaxis.set_major_locator(MaxNLocator(5)) 
            ax.text(-0.5, 1.2, corner_text, transform=ax.transAxes, size=9)
        plt.tight_layout(pad=0.1)
        pdf_object.savefig()
        pdf_object.close()
        matplotlib.use('qt5agg')
                
        if save_data_into_txt:
            for key in ['Velocity ccf radial','Distance']:
                if key == 'Velocity ccf radial':
                    filename=wd+fig_dir+'/data_accessibility/figure_9ab.txt'
                if key == 'Distance':
                    filename=wd+fig_dir+'/data_accessibility/figure_9cd.txt'
                file1=open(filename, 'w+')

                file1.write('#Time (ms)\n')
                for i in range(1, len(time_vec)):
                    file1.write(str(time_vec[i])+'\t')
                    
                file1.write('\n#Median\n')
                for i in range(1, len(y_vector[key]['median'])):
                    file1.write(str(y_vector[key]['median'])+'\t')
                    
                file1.write('\n#10th perc.\n')
                for i in range(1, len(y_vector[key]['10th'])):
                    file1.write(str(y_vector[key]['10th'])+'\t')
                    
                file1.write('\n#90th perc.\n')
                for i in range(1, len(y_vector[key]['90th'])):
                    file1.write(str(y_vector[key]['90th'])+'\t')    
                    
                file1.write('\n#Distribution bins\n')
                for i in range(1, len(y_vector[key]['bins'])):
                    file1.write(str(y_vector[key]['bins'])+'\t')
                file1.write('\n#Distribution\n')
                
                for i in range(len(y_vector[key]['data'][0,:])):
                    string=''
                    for j in range(len(y_vector[key]['data'][:,0])):
                        string+=str(y_vector[key]['data'][j,i])+'\t'
                    string+='\n'
                    file1.write(string)   
                file1.close()
      
    """
    Dependence on the r-r_sep and v_rad vs. rotation
    """
    if plot_figure == 10:
        plot_angular_vs_translational_velocity(tau_range=[-200e-6,200e-6],
                                               subtraction_order=2,
                                               plot_for_pop_paper=True,
                                               plot_log_omega=True,
                                               figure_filename=wd+fig_dir+'/fig_parameter_dependence.pdf')
            
        #No need for data accessibility txt file because the data are in the previous txt files.
    """
    Dependence on plasma parameters
    """
    if plot_figure == 11:
        raise NoobError('The idiot should have already finished this...')
   
    """
    Form factors vs. experimental observations
    """
    if plot_figure == 12:
        pass    