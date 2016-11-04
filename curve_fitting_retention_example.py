### Curve Fitting for retention ###

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

### Read in data ###

xdata = np.array([1,3,7,14])
ydata = np.array([0.38,0.22,0.17,0.12])

### Define concept type = power functions ###

def curve(x, a, b, c):
    return a * np.exp(-b * x) + c

### Fit that curve! ###

popt, pcov = curve_fit(curve, xdata, ydata)

### Get the new curve ###

xcurve = np.linspace(1,30,30)
ycurve = curve(xcurve, popt[0],popt[1],popt[2])

plt.plot(xcurve,ycurve*100)
plt.ylabel('Retention')
plt.xlabel('days since install')
plt.show()