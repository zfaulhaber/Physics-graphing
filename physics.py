import matplotlib.pyplot as plt
import numpy as np
import pickle
import math
from ctypes import cdll

lib = cdll.LoadLibrary("target/release/physics.dll")

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
t = np.linspace(0, 100, 10000)
vy = v * math.sin(th)
y = h + vy*t + .5*g*t**2
vx = v * math.cos(th)
x = vx * t
doubleth = th * 2
r = ((v**2 * math.sin(doubleth)) / (g * -1)) + 5
hmax = (v**2 * math.sin(th)**2) / (2 * (g * -1)) + 20
plt.ylim(bottom=0)
plt.xlim(left=0)
if h > 0:
    plt.ylim(top=(hmax + 25))
else:
    plt.ylim(top=(hmax + 5))
if h > 0:
    plt.xlim(right=(r + 30))
else:
    plt.xlim(right=r)
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.plot(x, y)
plt.grid()
plt.show()
