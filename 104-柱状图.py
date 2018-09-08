import numpy as np
import matplotlib.pyplot as plt
# 使用random seed可以是一切变得确定化
np.random.seed(0)

mu = 200
sigma = 25
x = np.random.normal(loc=mu,scale= sigma, size=100)

# 画多幅图片的第二种方法，返回的是一个fig对象和一个axes类型的ndarray对象
fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(8, 4))

ax0.hist(x, 20, normed=1, histtype='stepfilled', facecolor='g', alpha=0.75)
ax0.set_title('stepfilled')

# Create a histogram by providing the bin edges (unequally spaced).
bins = [100, 150, 180, 195, 205, 220, 250, 300]
ax1.hist(x, bins, normed=1, histtype='bar', rwidth=0.8)
ax1.set_title('unequal bins')

fig.tight_layout()
plt.show()
