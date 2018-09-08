import numpy  as np
from pylab import *

Y2016 = [15600, 12700, 11300, 4270, 3620]
Y2017 = [17400, 14800, 12000, 5200, 4020]
labels = ['Beijing', 'Shanghai', 'Hongkong', 'Shenzhen', 'Guangzhou']
bar_width = 0.5
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
plt.bar(np.arange(5), Y2016, label='2016', color='steelblue', alpha=0.8, width=bar_width)
plt.bar(np.arange(5) + bar_width, Y2017, label='2017', color='indianred', alpha=0.8, width=bar_width)
plt.xlabel('Top5 City')
plt.ylabel('Family Amount')
plt.xticks(np.arange(5) + bar_width, labels)
plt.ylim([2500, 20000])
plt.title('Millions Family Amount Top5 City Distribution')
# 为每个条形图添加数值标签
for x2016, y2016 in enumerate(Y2016):
    plt.text(x2016, y2016 + 100, '%s' % y2016)
for x2017, y2017 in enumerate(Y2017):
    plt.text(x2017 + bar_width, y2017 + 100, '%s' % y2017)
# 显示图例
plt.legend()
plt.show()
