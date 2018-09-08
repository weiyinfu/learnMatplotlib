"""
为了兼容matlab创造的一个库
"""
from matplotlib import mlab
import numpy as np

# 实现去中心化
a = np.random.random((10, 3))
b = mlab.demean(a, axis=0)
print(a)
print('=' * 10)
print(b)
print('=' * 10)
print(a - np.tile(np.mean(a, axis=1), (3, 1)).reshape(a.shape))
