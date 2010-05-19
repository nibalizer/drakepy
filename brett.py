from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = Axes3D(fig)

####
u = np.linspace(0, np.pi*2/3, 100)
v = np.linspace(0, np.pi*2/3*1/3, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='r')
####
u = np.linspace(np.pi*2/3*1/3, np.pi*2/3*2/3, 100)
v = np.linspace(np.pi*2/3*1/3, np.pi*2/3*2/3, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='g')
####
u = np.linspace(np.pi*2/3*2/3, np.pi*2/3*3/3, 100)
v = np.linspace(np.pi*2/3*2/3, np.pi*2/3*3/3, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='y')

####
u = np.linspace(np.pi*2/3, np.pi*4/3, 100)
v = np.linspace(0, np.pi*2/3, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')
####
u = np.linspace(np.pi*4/3, np.pi*6/3, 100)
v = np.linspace(0, np.pi*2/3, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')
####
u = np.linspace(0, np.pi*6/3, 100)
v = np.linspace(np.pi*2/3, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='b')
####


plt.show()

