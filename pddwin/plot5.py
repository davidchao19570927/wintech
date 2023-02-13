import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

plt.ion()

for i in range(100):
  x.append(i)
  y.append(i**2)
  plt.clf()
  plt.plot(x, y * np.array([-1]))
  plt.pause(0.001)
  plt.ioff()
