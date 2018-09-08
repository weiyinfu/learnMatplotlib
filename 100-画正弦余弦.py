import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

#fig对象用来进行一些全局的设置（例如图片大小）
#使用figsize设置图片大小，单位是英尺（30cm）
plt.figure(figsize=(8,6))
#使用$$表示写latex公式，记住plot有三个属性label，color，linewidth
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
#使用b--表示蓝色的--线
plt.plot(x,z,"b--",label="$cos(x^2)$")
plt.xlabel("Time(s)")#横轴表示的意义
plt.ylabel("Volt")#纵轴表示的意义
plt.title("PyPlot First Example")
plt.ylim(-1.2,1.2)#设置坐标轴的范围，这样可以禁止缩放
# plt.legend()#使用legend才会把label标上去，否则没有label
plt.show()