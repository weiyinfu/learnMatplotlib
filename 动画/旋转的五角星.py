import numpy as np
import pylab as plt
from matplotlib.animation import FuncAnimation

n = 5
a = np.linspace(0, np.pi * 2, n + 1)[:n]
fig = plt.figure(figsize=(3, 3))


def get(theta):
    return np.cos(theta), np.sin(theta)


five = [(get(a[i]), get(a[(i + 2) % len(a)])) for i in range(len(a))]
five_lines = []
for i in five:
    five_lines.append(plt.plot([i[0][0], i[1][0]], [i[0][1], i[1][1]])[0])


def update(frame_index):
    now = frame_index * np.pi / 20
    aa = now + a
    five = [(get(aa[i]), get(aa[(i + 2) % len(aa)])) for i in range(len(aa))]
    for line, points in zip(five_lines, five):
        line.set_xdata([points[0][0], points[1][0]])
        line.set_ydata([points[0][1], points[1][1]])


animation = FuncAnimation(fig, update, interval=10)
plt.axis('off')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.show()
