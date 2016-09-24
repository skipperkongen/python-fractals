import matplotlib.pyplot as plt
import random

x1,y1 = 0,0
x2,y2 = 0,100
x3,y3 = 100,100
x4,y4 = 100,0
x,y = x1,y1

xvec = [x1,x2,x3,x4]
yvec = [y1,y2,y3,y4]

for i in range(25000):
    rand = random.random()

    if rand <= 1/4:
        x = (x + x1) / 2
        y = (y + y1) / 2
    elif rand <= 2/4:
        x = (x + x2) / 2
        y = (y + y2) / 2
    elif rand <=3/4:
        x = (x + x3) / 2
        y = (y + y3) / 2
    else:
        x = (x + x4) / 2
        y = (y + y4) / 2

    xvec.append(x)
    yvec.append(y)

plt.plot(xvec, yvec, 'ko', markersize=1)
plt.show()
