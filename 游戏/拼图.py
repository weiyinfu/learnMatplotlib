import math
import random

import matplotlib.animation as animation
import numpy as np
import pylab as plt
from matplotlib.patches import Rectangle


def down(a: np.ndarray):
    for y in range(4):
        ans = []
        merged = False
        for x in range(3, -1, -1):
            if a[x][y]:
                if ans and ans[-1] == a[x][y] and not merged:
                    merged = True
                    ans[-1] *= 2
                else:
                    ans.append(a[x][y])
        while len(ans) < 4:
            ans.append(0)
        a[:, y] = ans[::-1]


def rotate(a: np.ndarray):
    b = np.empty_like(a)
    for i in range(4):
        for j in range(4):
            b[i][j] = a[j][3 - i]
    return b


def generate(a: np.ndarray):
    # 随机产生一个元素
    b = a.reshape(-1)
    ind = np.argwhere(b == 0).reshape(-1)
    b[ind[np.random.randint(0, len(ind))]] = 2


def rotate_many(a: np.ndarray, times: int):
    for i in range(times):
        a = rotate(a)
    return a


def no_same(a):
    # 判断是否存在相邻且相等的元素
    for i in range(4):
        for j in range(4):
            if i + 1 < 4 and a[i][j] == a[i + 1][j]:
                return False
            if j + 1 < 4 and a[i][j] == a[i][j + 1]:
                return False
    return True


def get_color_list(cnt):
    # 获取可用的颜色列表，在三维空间中均匀地选择若干个点
    a = []
    c = cnt ** (1 / 3)
    cc = math.ceil(c)

    def get(x):
        ans = hex(math.floor((x + 1) / cc * 255))[2:]
        if len(ans) < 2:
            return '0' + ans
        return ans

    for i in range(cc):
        for j in range(cc):
            for k in range(cc):
                now = f"#{get(i)}{get(j)}{get(k)}"
                a.append(now)
    # 保证每次颜色一致性
    random.seed(0)
    random.shuffle(a)
    return a[:cnt]


color_list = get_color_list(20)


def color2vec(s: str):
    # 颜色字符串转int数组
    a = np.array([int(s[i:i + 2], base=16) for i in range(1, len(s), 2)])
    return a


def get_fore(back_color: str):
    # 根据背景色距离黑白两色的距离来决定前景色使用黑色还是白色
    white_dis = np.linalg.norm(color2vec(back_color) - 255)
    black_dis = np.linalg.norm(color2vec(back_color) - 0)
    fore_color = 'white' if white_dis > black_dis else 'black'
    return fore_color


def get_color(v):
    # 返回前景色和背景色
    if v == 0:
        return 'white', 'black'
    ind = math.floor(math.log2(v))
    ind = np.clip(ind, 0, len(color_list))
    back_color = color_list[ind]
    return get_fore(back_color), back_color


class Game2048:
    def is_over(self) -> bool:
        return np.count_nonzero(self.a == 0) == 0 and no_same(self.a)

    def update(self, *args, **kwargs):
        self.axes.cla()
        self.axes.axis('off')
        for i in range(4):
            for j in range(4):
                x, y = j / 4, 1 - i / 4
                v = self.a[i, j]
                fore, back = get_color(v)
                self.axes.add_patch(Rectangle((x, y - 0.25), 0.25, 0.25,
                                              facecolor=back,
                                              edgecolor='grey',
                                              fill=True,
                                              lw=1))
                if v != 0:
                    self.axes.text(x + 0.125, y - 0.125, v, ha='center', va='center', fontsize='20', color=fore, fontweight='bold')
        if self.game_over:
            x, y = 0.5, 0.5
            w, h = 0.4, 0.2
            self.axes.add_patch(Rectangle((x - w / 2, y - h / 2), w, h,
                                          facecolor='grey',
                                          edgecolor='white',
                                          fill=True,
                                          alpha=0.5,
                                          lw=1))
            self.axes.text(x, y, 'Game Over', ha='center', va='center', fontsize='20', color='white', fontweight='bold')
            self.axes.text(x, y - 0.08, 'Press Enter To Restart', ha='center', va='center', fontsize='10', color='white', fontweight='bold')

    def on_cmd(self, cmd):
        cmd = cmd.key
        if self.game_over:
            if cmd == 'enter':
                self.init()
            return
        ops = ["up", 'right', 'down', 'left']
        if cmd not in ops:
            return
        ind = ops.index(cmd)
        times = (2 - ind + 4) % 4
        b = rotate_many(self.a, (4 - times) % 4)
        down(b)
        self.a = rotate_many(b, times)
        if np.count_nonzero(self.a == 0):
            generate(self.a)
        self.game_over = self.is_over()

    def init(self):
        self.a = np.zeros((4, 4), dtype=np.int32)
        self.game_over = False
        generate(self.a)

    def main(self):
        self.init()
        fig, self.axes = plt.subplots(figsize=(8, 8), facecolor='black')
        fig.canvas.mpl_connect('key_press_event', self.on_cmd)
        _ = animation.FuncAnimation(fig, self.update, interval=200)
        plt.show()


Game2048().main()
