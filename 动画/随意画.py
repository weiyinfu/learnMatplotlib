import numpy as np
import pylab as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(3, 3))


def update(frame_index):
    if frame_index % 100 == 0:
        fig.clear()
        plt.axis('off')
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)
    x, y, r = np.random.random(3) * 2 - 1
    r = abs(r)
    plt.scatter(x, y, s=r * 100)


animation = FuncAnimation(fig, update, interval=50)
plt.axis('off')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.show()
