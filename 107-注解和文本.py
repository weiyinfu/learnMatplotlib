import matplotlib.pyplot as plt
# 定义决策树决策结果的属性，用字典来定义
# 下面的字典定义也可写作 decisionNode={boxstyle:'sawtooth',fc:'0.8'}
# boxstyle为文本框的类型，sawtooth是锯齿形，fc是边框线粗细
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
di_edge = dict(arrowstyle="<-")  # 有向边
edge = dict(arrowstyle="--")  # 无向边

fig = plt.figure(1, facecolor='white')  # 定义一个画布，背景为白色
fig.clf()  # 把画布清空
# createPlot.ax1为全局变量，绘制图像的句柄，subplot为定义了一个绘图，
# 111表示figure中的图有1行1列，即1个，最后的1代表第一个图
# frameon表示是否绘制坐标轴矩形
ax1 = plt.subplot(111, frameon=False)
#annotate是注解，用来对图像进行一些注释
ax1.annotate('a decision node',
             xy=(0.5, 0.1),  # 终点的坐标
             xycoords='axes fraction',
             xytext=(0.1, 0.5),  # 起点的坐标
             textcoords='axes fraction',
             va="center", ha="center",  # 文本对齐方式
             bbox=decisionNode,#框的类型
             arrowprops=di_edge#边的类型：有向边
             )
ax1.annotate("a leaf node",
             xy=(0.8, 0.1),
             xycoords='axes fraction',
             xytext=(0.3, 0.8), textcoords='axes fraction',
             va="center", ha="center",
             bbox=leafNode, arrowprops=di_edge)
ax1.text(0.5, 0.5, "hello world", va="center", ha="center", rotation=30)
plt.show()
