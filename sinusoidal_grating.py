'''

Simple function to generate sinusoidal grating visual stimulus

parameters:

x,y      :  Two dimensional grid of photoreceptors
theta    :  Orientation
K        :  Spatial frequency
phi      :  Spatial phase
A        :  Contrast amplitude

returns:

sinusoidal grating corresponding to the given parameters ( mentioned above)

'''

import numpy as np
import matplotlib.pyplot as plt
import math as m

x0 = 5  # given x0=5,y0=5
y0 = 5

delta_x = 1/10  # Sampling
delta_y = 1/10

max_x = (2*x0)/delta_x  # as per visual field description given
max_y = (2*y0)/delta_y

def grid_generation():
    # Function to generate the 2-D grid [x,y]
    x_range=np.arange(-x0,x0,delta_x)
    y_range=np.arange(-y0,x0,delta_y)
    x,y=np.meshgrid(x_range,y_range)
    return x,y

def sinusoidal_grating(theta,k,phi):
    '''Function to compute sinusoidal grating with arguments theta(orientation),
       k(spatial x,y=grid_generation() #generating [x,y] grid '''
    A=1 #Amplitude
    sin_grating=A*np.cos(k*x*np.cos(theta)+k*y*np.sin(theta)-phi)
    return sin_grating




