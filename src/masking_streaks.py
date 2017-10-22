import numpy as np
from matplotlib import pyplot as plt
#from radial_integration import *
#from pies_and_rings import *
import skbeam.core.utils as utils

def mask_streaks(data,mask=None,center = [1364,1504],threshold=3.5,dphi=2):
    '''
    masking the streaks based on a threshold by introducing 
    a pie slice mask for the points over the treshold. 
    '''
    # -- Definitions
    nx,ny = data.shape[0],data.shape[1]
    phi_mask = np.ones(data.shape,dtype=bool)

    # -- radial integration (azimuthal dependence)
    angles,Intensity=radial_average(data,mask=mask,center=center)
    if np.average(Intensity)>0:
        Intensity/=np.average(Intensity)
        angles_to_mask = angles[Intensity>threshold]

        if len(angles_to_mask)>0:
            # -- angular map
            phi = utils.angle_grid(center, data.shape)* 180 / np.pi+180

            # -- streak mask
            for i in range(len(angles_to_mask)):
                phi_mask *= take_pie_slice(nx,ny,phi,angles_to_mask[i]-dphi,angles_to_mask[i]+dphi)

    return phi_mask





def radial_average(image,mask=None, center=[1364,1504],threshold=0, nx=300,
                             pixel_size=(1, 1),  min_x=-np.pi, max_x=np.pi):
    '''
    Does the radial average over a given range, including threshold masking
    '''
    # - create angular grid
    phi_val = utils.angle_grid(center, image.shape,pixel_size)#*180./np.pi+180.
    # - create unitary mask (in case it's none)
    if mask is None:
        mask=np.ones(image.shape)

    # - bin values of image based on the angular coordinates
    bin_edges, sums, counts = utils.bin_1D(np.ravel(phi_val*mask),
                                           np.ravel(image*mask), nx,
                                           min_x=min_x,
                                           max_x=max_x)
    th_mask = counts > threshold
    phi_averages = np.array(sums[th_mask],dtype=float)/ np.array(counts[th_mask],dtype=float)
    bin_centers = utils.bin_edges_to_centers(bin_edges)[th_mask]

    return bin_centers*180/np.pi+180., phi_averages
    #return bin_centers, phi_averages


def take_pie_slice(nx,ny,phi,i_angle,f_angle):
    '''
    Takes a pie slice between given initial and final angle
    '''
    pie_slice = np.zeros((nx,ny),dtype=bool)
    pie_slice[phi<=i_angle]=1
    pie_slice[phi>f_angle]=1
    return pie_slice

