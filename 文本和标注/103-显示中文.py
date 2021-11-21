from pylab import *

# 搜索plt rcParams查看更多plt配置
plt.rcParams['font.sans-serif'] = 'HanziPen SC,STFangsong,Baoli SC'.split(",")  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.plot(arange(0, 10, 0.1), sin(arange(0, 10, 0.1)))
plt.title("天下大势为我所控")
plt.show()
