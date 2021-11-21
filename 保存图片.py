import io

import numpy as np
import pylab as plt
from PIL import Image

"""
第一种方式：直接savefig
"""
fig = plt.figure()
cout = io.BytesIO()
# plt.savefig(cout)
# 或者下面这一行
fig.savefig(cout)
img = Image.open(cout)
a = np.array(img)
print(a.shape)

"""
第二种方式：canvas.print_png()
"""
cout = io.BytesIO()
fig.canvas.print_png(cout)
img = Image.open(cout)
a = np.array(img)
print(a.shape)

print(dir(fig))
