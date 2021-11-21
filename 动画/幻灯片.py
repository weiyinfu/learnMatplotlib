import pylab as plt
from matplotlib.animation import FuncAnimation
from skimage import data

a = [data.astronaut(), data.camera(), data.rocket()]
fig = plt.figure(figsize=(3, 3))


def update(frame_index):
    plt.imshow(a[frame_index % len(a)])


animation = FuncAnimation(fig, update, interval=1000)
plt.axis('off')
plt.show()
