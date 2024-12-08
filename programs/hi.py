import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, mean, amplitude, sigma):
    """
    Calculate the Gaussian function.

    Parameters:
    x (array-like): Input array of x values.
    mean (float): Mean of the Gaussian distribution.
    amplitude (float): Amplitude of the Gaussian peak.
    sigma (float): Standard deviation of the Gaussian distribution.

    Returns:
    numpy.ndarray: Gaussian function values corresponding to the input x values.
    """
    return amplitude * np.exp(- (x - mean)**2 / (2 * sigma ** 2))

def exp_bkg(x, amplitude, b):
    """
    Calculate the exponential background function.

    Parameters:
    x (array-like): Input array of x values.
    amplitude (float): Amplitude of the exponential function.
    b (float): Exponential decay constant.

    Returns:
    numpy.ndarray: Exponential function values corresponding to the input x values.
    """
    return amplitude * np.exp(-b * x)

def data_shape(x, mean1, mean2, amp1, sigma1, sigma2, amp2, b):
    """
    Combine Gaussian and exponential functions to mimic b-meson invariant mass distribution.

    Parameters:
    x (array-like): Input array of x values.
    mean1 (float): Mean of the first Gaussian peak.
    mean2 (float): Mean of the second Gaussian peak.
    amp1 (float): Amplitude of the first Gaussian peak.
    sigma1 (float): Standard deviation of the first Gaussian peak.
    sigma2 (float): Standard deviation of the second Gaussian peak.
    amp2 (float): Amplitude of the exponential background.
    b (float): Exponential decay constant.

    Returns:
    numpy.ndarray: Combined function values corresponding to the input x values.
    """
    g1 = gaussian(x, mean1, amp1, sigma1)
    g2 = gaussian(x, mean2, amp1 * 0.5, sigma2)
    g3 = gaussian(x, mean2 + 0.2, amp1 * 0.4, sigma2)
    b1 = exp_bkg(x, amp2, b)
    return g1 + g2 + g3 + b1

params = [5.25, 4.25, 1., 0.05, 0.065, 1.5e4, 2.47]

# Solution to 1.

x=np.linspace(4.0,6.0,10000)
plt.plot(x,data_shape(x,5.25, 4.25, 1., 0.05, 0.065, 1.5e4, 2.47))