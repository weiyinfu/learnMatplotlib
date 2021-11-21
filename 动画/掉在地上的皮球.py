import pylab as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure(figsize=(3, 3))
x, y = 0, 2  # 小球的位置
v = 0  # 小球的速度
p = plt.scatter(x, y, s=500)  # 把小球画出来
plt.plot([-1, 1], (-0.25, -0.25))  # 画一条地平线
dt = 0.1  # 每个间隔的时间
g = 1  # 重力系数


def update(frame_index):
    global y, v
    need_time = ((v * v + 2 * g) ** 0.5 - v) / g  # 到落地需要的时间
    need_time = min(abs(need_time), dt)
    left_time = dt - need_time  # 转向需要的时间
    vv = v - g * need_time
    y += (vv + v) / 2 * need_time
    v = vv
    if y <= 1e-7:
        v *= -0.91
        y += v * left_time
    p.set_offsets([x, y])


animation = FuncAnimation(fig, update, interval=50)
plt.axis('off')
plt.xlim(-1, 1)
plt.ylim(-0.5, 2.5)
plt.show()
