import matplotlib.pyplot as plt
import numpy as np
import pickle
import math
from ctypes import cdll

lib = cdll.LoadLibrary("physics.dll")

lib.do_all()

filename = "info"
fileObject = open(filename, 'rb')
depickled = pickle.load(fileObject)
keys = list(depickled.keys())
values = list(depickled.values())
count = 0
v = 0
h = 0
g = -9.8
th = 0
for item in keys:
    a = str(item)
    if a.startswith('v'):
        v = values[count]
        count += 1
    elif a.startswith('h'):
        h = values[count]
        count += 1
    elif a.startswith('t'):
        th = values[count]
        count += 1
t = np.linspace(0, 15, 30)
vy = v * math.sin(th)
y = h + vy*t + .5*g*t**2
hmax = (v**2 * math.sin(th)**2) / (2 * (g * -1)) + 20
plt.ylim(bottom=0)
plt.ylim(top=hmax)
plt.xlim(left=0)
plt.xlim(right=25)
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.plot(t, y)
plt.show()
