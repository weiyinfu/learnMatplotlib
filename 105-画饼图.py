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
