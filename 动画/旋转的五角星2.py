import numpy as np
import pylab as plt
from matplotlib.animation import FuncAnimation

n = 5
a = np.linspace(0, np.pi * 2, n + 1)[:n]
fig = plt.figure(figsize=(3, 3))


def get(theta):
    return np.cos(theta), np.sin(theta)


def get_data(a):
    points = []
    five = np.array([(get(a[i]), get(a[(i + 2) % len(a)])) for i in range(len(a))])
    for i in five:
        points.append(i[:, 0])
        points.append(i[:, 1])
    return points


def update(frame_index):
    fig.clear()
    plt.axis('off')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    now = frame_index * np.pi / 20
    plt.plot(*get_data(now + a))


animation = FuncAnimation(fig, update, interval=10)
plt.show()
