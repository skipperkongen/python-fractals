import matplotlib.pyplot as plt
import random

x1,y1 = 0,0
x2,y2 = 50,100
x3,y3 = 100,0
x,y = x1,y1

xvec = [x1,x2,x3]
yvec = [y1,y2,y3]

for i in range(50000):
    rand = random.random()

    if rand <= 1/3:
        x = (x + x1) / 2
        y = (y + y1) / 2
    elif rand <= 2/3:
        x = (x + x2) / 2
        y = (y + y2) / 2
    else:
        x = (x + x3) / 2
        y = (y + y3) / 2

    xvec.append(x)
    yvec.append(y)

plt.plot(xvec, yvec, 'ko', markersize=1)
plt.show()
