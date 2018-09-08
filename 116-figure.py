from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0, 5, 0.1)

plt.figure(1)  # 创建了图1（figure（1））
plt.subplot(211)  # 在figure1种生成子图1
plt.plot(x, np.sin(x))  # 在当前子图，也就是子图1种画图
plt.subplot(212)  # 在figure1中生成子图2
plt.plot(x, x ** 2)

plt.figure(2)
plt.subplot(131)
plt.plot(x, x)
plt.subplot(132)
plt.plot(x, 2 * x + 1)
plt.subplot(133)
plt.plot(x, np.cos(x))

plt.show()
