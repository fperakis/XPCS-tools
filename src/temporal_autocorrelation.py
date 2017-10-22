import numpy as np
#from nexusformat.nexus import *
from matplotlib import pyplot as plt
#from angular_integration import *
from parameters import *

# analysis tools adapted from scikit-beam
# (https://github.com/scikit-beam/scikit-beam/tree/master/skbeam/core)
import skbeam.core.roi as roi
import skbeam.core.correlation as corr
import skbeam.core.utils as utils


def calculate_g2(data,mask=None,center=None):
    '''
    Calculates the intensity-intensity temporal autocorrelation using
    scikit-beam packages for a series of Q's
    '''

    # -- parameters
    dpix,Ldet,center_new  = eiger_parameters()
    if center==None:
        center = center_new
    energy,wavelenght = xray_parameters()
    inner_radius,width,spacing,num_rings,num_levels = g2_parameters()

    # -- ring array
    edges = roi.ring_edges(inner_radius, width, spacing, num_rings)
    rings = roi.rings(edges, center, data[0].shape)
    ring_mask = rings*mask

    # -- convert ring to q
    two_theta = utils.radius_to_twotheta(Ldet, edges*dpix)
    q_val = utils.twotheta_to_q(two_theta, wavelenght)
    qt = np.mean(q_val, axis=1)

    # -- calculate g2
    num_bufs = data.shape[0]
    g2, dt = corr.multi_tau_auto_corr(num_levels,num_bufs,ring_mask,mask*data)

    return qt,dt[1:],g2[1:],ring_mask

def calculate_two_time_g2(data,mask=None,center=None):
    '''
    Calculates the two-time intensity-intensity temporal autocorrelation using
    scikit-beam packages for a series of Q's
    '''

    # -- parameters
    dpix,Ldet,center_new  = eiger_parameters()
    if center==None:
        center = center_new
    energy,wavelenght = xray_parameters()
    inner_radius,width,spacing,num_rings,num_levels = g2_parameters()

    # -- ring array
    edges = roi.ring_edges(inner_radius, width, spacing, num_rings)
    rings = roi.rings(edges, center, data[0].shape)
    ring_mask = rings*mask

    # -- convert ring to q
    two_theta = utils.radius_to_twotheta(Ldet, edges*dpix)
    q_val = utils.twotheta_to_q(two_theta, wavelenght)
    qt = np.mean(q_val, axis=1)

    # -- calulate g2
    num_bufs = data.shape[0]
    n_frames = data.shape[0]

    g2_t12=np.array(corr.two_time_corr(ring_mask,mask*data,n_frames,num_bufs,num_levels)[0])

    return qt,g2_t12,ring_mask



