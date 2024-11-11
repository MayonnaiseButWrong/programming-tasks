# YOUR CODE HERE
'''
Script:
Demonstrate a solar irradiance random number generator.
'''
import numpy as np
from random import random, uniform
import matplotlib.pyplot as plt

# get data from file
alldata = np.loadtxt("am15.csv", delimiter=",", dtype="float64") # file should be downloaded together with notebook exercise.

bin_edges = alldata[:,0] # [nm]
spectrum  = alldata[:,1] # W/m^2/nm

# step 1
bindifferences = np.diff(bin_edges)
bindifferences = np.insert(bindifferences, 0, 0)
norm = np.sum(spectrum * bindifferences) # YR: this variable is needed in the test, leave name unchanged.
normalized = spectrum / norm

# step 2
cumulative = np.cumsum(normalized * bindifferences)

store = []
nsims = 100000 # YR: for a good test plot need a lot of simulations, leave unchanged for submission.
for _ in range(nsims):
    # step 4
    trial = random()
    print(trial)
    # step 5
    randomxval = np.where(cumulative >= trial)[0]
    upperbin = bin_edges[1 + randomxval[0]] # last of all <= trial
    lowerbin = bin_edges[randomxval[0]] # first of all >= trial

    # step 6
    value = uniform(lowerbin, upperbin)
    store.append(value)

# YR: no error below this line, variable 'data' is needed in test, leave name unchanged.
data = np.array(store)
plt.hist(data, bins=bin_edges, log=True)
plt.xlabel('wavelength [nm]', fontsize=12)
plt.ylabel('emission spectrum', fontsize=12)
plt.show()