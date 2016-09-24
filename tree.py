import matplotlib.pyplot as plt
import random
import numpy

x,y = 0, 0

xvec = [x]
yvec = [y]

length = 1
decay = 0.99

for i in range(50000):
    rand = random.random()

    if rand < 0.005:
        length = 1
        newx,newy = 0,0
    elif rand < 0.5:
        newx = x + decay
        newy = y + length
        length = length * decay
    else:
        newx = x - decay
        newy = y + length
        length = length * decay

    x = newx
    y = newy

    xvec.append(x)
    yvec.append(y)

plt.plot(xvec, yvec, 'ko', markersize=1)
plt.show()
