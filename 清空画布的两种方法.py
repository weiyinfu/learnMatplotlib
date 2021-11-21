import pylab as plt

fig, axes = plt.subplots()
axes.set_xlim(-3, 3)
axes.set_ylim(-3, 3)
axes.plot([0, 1], [0, 1])
plt.pause(2)
# axes.cla()
axes.clear()
# fig.clear()
axes.figure.canvas.draw()  # 直接重绘
axes.plot([1, 2], [1, 2])
plt.show()
