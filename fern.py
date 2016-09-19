import matplotlib.pyplot as plt
import random

x, y = random.random(), random.random()

xvec = [x]
yvec = [y]

for i in range(50000):
    rand = random.random()
    if rand < 0.01:
        x, y = 0.0, 0.16 * y;
    elif rand < 0.86:
        newx = (0.85 * x) + (0.04 * y)
        newy = (-0.04 * x) + (0.85 * y) + 1.6
        x, y = newx, newy
    elif rand < 0.93:
        newx = (0.2 * x) - (0.26 * y)
        newy = (0.23 * x) + (0.22 * y) + 1.6
        x, y = newx, newy
    else:
        newx = (-0.15 * x) + (0.28 * y)
        newy = (0.26 * x) + (0.24 * y) + 0.44
        x, y = newx, newy

    xvec.append(x)
    yvec.append(y)

plt.plot(xvec, yvec, 'ko', markersize=1)
plt.show()
