import shutil

import matplotlib
import pylab as plt

print(plt.rcParams.keys())
print(matplotlib.get_cachedir())
shutil.rmtree(matplotlib.get_cachedir())
