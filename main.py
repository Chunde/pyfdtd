import math
import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.colors as colors
import pyfdtd

# source function
def f(t):
    x = t - 1000e-12
    return math.exp(-x**2/(2.0*200.0e-12**2))*math.cos(2.0*math.pi*20e9*x)

# material function
def mat(x, y):
    if (x-0.2)**2 + (y-0.15)**2 < 0.15**2 and (x-0.2)**2 + (y-0.35)**2 < 0.15**2:
        return 2.0

    return 1.0
        
# create solver
solver = pyfdtd.solver(pyfdtd.field(0.4, 0.8, deltaX=0.001))

# add material
solver.material['epsilon'] = mat

# add source
solver.ports.append(pyfdtd.port(0.2, 0.1, function=f))

# iterate
history = solver.solve(7e-9, saveHistory=True)

# show plot
fig = plt.figure(1)

ims = []
for f in history:
    im = plt.imshow(f, norm=colors.Normalize(-0.01, 0.01))
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=20)

plt.show()
