import numpy as np
from matplotlib import pyplot as plt

def eiger_parameters():
    dpix = 0.075                 # the physical size of the pixels
    Ldet = 5000.                 # detector to sample distance 
    center = [1364,1504]         # center in pixel units

    parameters = [dpix,Ldet,center]
    return parameters

def xray_parameters():
    h = 4.135667516*1e-18        # kev*sec
    c = 3*1e8                    # m/s
    energy = 8.0                 # keV
    wavelenght = h*c/energy*1e10 # wavelength of the X-rays (A-1)

    parameters = [energy,wavelenght]
    return parameters

def g2_parameters():
    inner_radius = 40           # radius of first ring
    width        = 20            # width of rings
    spacing      = 0             # spacing between rings
    num_rings    = 10             # number of rings
    num_levels   = 1             # number of levels to calculate g2

    parameters = [inner_radius,width,spacing,num_rings,num_levels]
    return parameters

