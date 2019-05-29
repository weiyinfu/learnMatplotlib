import matplotlib.pyplot as plt
import numpy as np

r = 10
n = 6
angles = np.linspace(0, 2 * np.pi, n)
xs = r * np.sin(angles)
ys = r * np.cos(angles)
ind = np.arange(0, n) * 2 % (n - 1)
print(ind)
fig=plt.figure()
plt.scatter(xs, ys)
plt.plot(xs[ind], ys[ind])
# plt.show()
fig.save('haha.svg')