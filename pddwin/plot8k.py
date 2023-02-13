from math import pi

import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

x = np.arange(0, 2*pi+pi/4, 2*pi/8)
y = np.sin(x)
s = interpolate.InterpolatedUnivariateSpline(x, y)
xnew = np.arange(0, 2*pi, pi/50)
ynew = s(xnew)
plt.figure()
plt.plot(x, y, 'x', xnew, ynew, xnew, np.sin(xnew), x, y, 'b')
plt.legend(['Linear', 'spline', 'True'])
plt.axis([-0.05, 6.33, -1.05, 1.05])
plt.title('InterpolatedUnivariateSpline')
plt.show()
