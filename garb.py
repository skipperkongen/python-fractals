import matplotlib.pyplot as plt
import random

x,y = .5, .5

xvec = [x]
yvec = [y]

for i in range(25000):
    rand = random.random()

    if rand < 0.01:
        x, y = 0.2*x, 0.16 * y;
    elif rand < 0.5:
        newx = (0.65 * x) + (0.02 * y)
        newy = (-0.04 * x) + (0.75 * y) + .9
        x, y = newx, newy
    else:
        newx = (0.85 * x) + (-0.04 * y)
        newy = (-0.08 * x) + (0.85 * y) + 1.6
        x, y = newx, newy

    xvec.append(x)
    yvec.append(y)

plt.plot(xvec, yvec, 'ko', markersize=1)
plt.show()
