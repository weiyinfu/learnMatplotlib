import matplotlib.pyplot as plt

labels = 'frogs', 'hogs', 'dogs', 'logs'
sizes = 15, 20, 45, 10
colors = 'yellowgreen', 'gold', 'lightskyblue', 'lightcoral'
explode = 0, 0.2, 0, 0
plt.pie(sizes,
        explode=explode,  # 向外拿出去
        labels=labels,  # 各个饼的标注
        colors=colors,  # 各个饼的颜色
        autopct='%1.1f%%',  # 数字格式化
        pctdistance=0.6,  # 数字所在距离中心的距离
        shadow=True,  # 显示饼图阴影
        labeldistance=1.2,  # 文字与饼图的相对位置
        startangle=50,
        radius=1,  # 整个饼图的半径
        counterclock=True,  # 顺时针画图
        center=(0.7, 0.8),  # 饼图中心位置
        )  # 饼图开始角度
plt.axis('equal')
plt.show()
"""
x: 指定绘图的数据

explode:指定饼图某些部分的突出显示，即呈现爆炸式

labels：为饼图添加标签说明，类似于图例说明

colors：指定饼图的填充色

autopct：设置百分比格式，如'%.1f%%'为保留一位小数

shadow：是否添加饼图的阴影效果

pctdistance:设置百分比标签与圆心的距离

labeldistance：设置各扇形标签（图例）与圆心的距离；

startangle：设置饼图的初始摆放角度, 180为水平；

radius：设置饼图的半径大小；

counterclock：是否让饼图按逆时针顺序呈现, True / False；

wedgeprops：设置饼图内外边界的属性，如边界线的粗细、颜色等, 如wedgeprops = {'linewidth': 1.5, 'edgecolor':'green'}

textprops：设置饼图中文本的属性，如字体大小、颜色等；

center：指定饼图的中心点位置，默认为原点

frame：是否要显示饼图背后的图框，如果设置为True的话，需要同时控制图框x轴、y轴的范围和饼图的中心位置；

"""
