import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

def line(x,a,b):
    return a*x+b

def gaussian(x,a,b):
    return np.exp(-x**2./(b**2))

def sigmoid(x,a,b):
    return 1/(1.+np.exp(np.abs(a)*(x-np.abs(b))))

def exponential(x,a,b):
    return np.abs(a)*np.exp(-x/(np.abs(b)))+1

def stretched_exponential(x,a,b,c):
    return np.abs(a)*np.exp(-(x/np.abs(b))**c)+1

def fit(function,x,y,p0=None,sigma=None,bounds=None):
    '''
    fits a function and return the fit resulting parameters and curve
    '''
    popt,pcov = curve_fit(function,x,y,p0=p0,sigma=sigma)
    x = np.arange(0,1e4)
    curve = function(x,*popt)
    perr = np.sqrt(np.diag(pcov))
    return popt,x,curve,perr
