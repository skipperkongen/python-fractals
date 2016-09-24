import matplotlib.pyplot as plt
import random

def play(alpha):

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
            x = (x + x1) / alpha
            y = (y + y1) / alpha
        elif rand <= 2/4:
            x = (x + x2) / alpha
            y = (y + y2) / alpha
        elif rand <=3/4:
            x = (x + x3) / alpha
            y = (y + y3) / alpha
        else:
            x = (x + x4) / alpha
            y = (y + y4) / alpha

        xvec.append(x)
        yvec.append(y)

    plt.plot(xvec, yvec, 'ko', markersize=1)
    plt.suptitle('Alpha = {}'.format(alpha))
    print("Saving image")
    plt.savefig('images/square-{0:.2f}.png'.format(alpha))
    plt.clf()

base = 1
stride = 0.01
for i in range(150):
    offset = stride * i
    play(base + offset)
