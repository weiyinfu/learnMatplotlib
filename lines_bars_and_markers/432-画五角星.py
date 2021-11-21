import matplotlib.pyplot as plt
import numpy as np


def get(n):
    ans = [1]
    for i in range(2, int(np.ceil(n / 2))):
        if np.gcd(n, i) == 1:
            ans.append(i)
    return ans


data_list = []
for n in range(3, 11):
    for delta in get(n):
        print(n, delta)
        angle = np.linspace(0, 2 * np.pi, n + 1)
        y = np.cos(angle)
        x = np.sin(angle)
        ind = np.arange(0, n + 1, 1) * delta % n
        data_list.append((x[ind], y[ind], f"n={n},delta={delta}"))
row = int(len(data_list) ** 0.5)
row = min(row, 4)
print(data_list)
col = int(np.floor(len(data_list) / row))
fig, axes = plt.subplots(col, row)
fig.set_size_inches(3 * row, 3 * col)
if type(axes) != np.ndarray:
    axes = np.array([axes])
axes = axes.reshape(-1)
for (x, y, title), a in zip(data_list, axes):
    a.plot(x, y)
    a.set_title(title)
    a.axis("off")
plt.show()
