"""
俄罗斯方块
"""
import logging
from typing import List, Tuple

import matplotlib.animation as animation
import numpy as np
import pylab as plt
from matplotlib.patches import Rectangle

log = logging.root
"""
俄罗斯方块一共有七种小块
I、J、L、O、S、T、Z

map编码说明：0表示空白，1表示静止的方块，2表示正在活跃的方块
"""
blocks = """
* 
*
*
*

*
***

  *
***

**
**

 **
**

 *
***

**
 **
""".splitlines()
directions = ((0, 1), (0, -1), (-1, 0), (1, 0))


def legal(x, y, map):
    return len(map) > x >= 0 and len(map[x]) > y >= 0


def get_object(x, y, map):
    # 在一个二维结构中找到一个块
    q = [(x, y)]
    ch = map[x][y]
    vis = set()
    vis.add((x, y))
    while q:
        x, y = q.pop()
        for dx, dy in directions:
            xx, yy = x + dx, y + dy
            if not legal(xx, yy, map) or (xx, yy) in vis:
                continue
            if map[xx][yy] != ch:
                continue
            vis.add((xx, yy))
            q.append((xx, yy))
    return list(vis)


def regularize(obj: List[Tuple[int, int]]):
    x, y = min(obj)
    return [(i - x, j - y) for i, j in obj]


def parse_blocks():
    ans = []
    vis = set()
    for i in range(len(blocks)):
        for j in range(len(blocks[i])):
            if blocks[i][j] == '*' and (i, j) not in vis:
                obj = list(get_object(i, j, blocks))
                for pos in obj:
                    vis.add(pos)
                ans.append(regularize(obj))
    return ans


block_list = parse_blocks()


def find_object(map: np.ndarray):
    # 在map中寻找物体
    return list(np.argwhere(map == 2))


def rotate(obj, map):
    # 首先计算出obj的中心，这个函数是一个尽力而为服务，返回是否旋转成功
    a = np.array(obj)
    x, y = np.mean(a, axis=0)
    x, y = int(x), int(y)
    b = []
    for i, j in obj:
        ii, jj = i - x, j - y
        xx, yy = x + jj, y - ii
        b.append((xx, yy))
    v = map[obj[0][0]][obj[0][1]]

    def roback():
        for x, y in obj:
            map[x][y] = v

    for i, j in obj:
        map[i][j] = 0
    for i, j in b:
        if not legal(i, j, map) or map[i][j]:
            roback()
            return False
    for i, j in b:
        map[i][j] = v
    return True


def generate(map):
    # 在map中生成一个物体，如果生成成功，则
    ind = np.random.randint(0, len(block_list))
    obj = block_list[ind]
    cx = 0
    cy = len(map[0]) // 2
    for x, y in obj:
        if map[x + cx][y + cy]:
            return False
    for x, y in obj:
        map[x + cx][y + cy] = 2  # 2表示当前的活跃object
    return True


def move(obj, dx, dy, map: np.ndarray):
    v = map[obj[0][0]][obj[0][1]]
    for x, y in obj:
        map[x][y] = 0

    def roback():
        for x, y in obj:
            map[x][y] = v

    for x, y in obj:
        xx, yy = x + dx, y + dy
        if not legal(xx, yy, map) or map[xx][yy]:
            roback()
            return False
    for x, y in obj:
        xx, yy = x + dx, y + dy
        map[xx][yy] = v
    return True


def disappear(a: np.ndarray):
    # 把一整行消除掉
    line = []
    for i in range(len(a)):
        if not np.all(a[i] == 1) and np.any(a[i] == 1):
            line.append(i)
    b = np.zeros_like(a)
    for ind, i in enumerate(line):
        j = len(line) - ind
        b[-j] = a[i]
    return b


class Teris:
    def is_over(self) -> bool:
        return self.over

    def update(self, *args, **kwargs):
        self.tick += 1
        self.axes.cla()
        # self.axes.axis('off')
        self.axes.xaxis.set_ticklabels([])
        self.axes.yaxis.set_ticklabels([])
        self.axes.grid()
        self.axes.set_xlim(0, self.cols)
        self.axes.set_ylim(0, self.rows)
        if not self.over and self.tick % 4 == 0:
            # 执行更新操作
            obj = find_object(self.map)  # list[pos]
            if not obj:  # 产生一个新的物体
                res = generate(self.map)
                if not res:
                    self.over = True
            else:
                if not move(obj, 1, 0, self.map):
                    # 如果没能移动成功，小块由活跃转向不活跃
                    self.after_down()
        # 执行绘图操作
        # 首先绘制一个外边框
        self.axes.add_patch(Rectangle((0, 0), self.cols, self.rows,
                                      facecolor='black',
                                      edgecolor='grey',
                                      fill=False,
                                      lw=3))
        # 然后绘制地图里面的每个小方块
        for (i, j), v in np.ndenumerate(self.map):
            if v == 0:
                continue
            x, y = j, self.rows - i - 1
            if v == 2:
                face_color = '#440000'
            else:
                face_color = 'grey'
            self.axes.add_patch(Rectangle((x, y), 1, 1,
                                          facecolor=face_color,
                                          edgecolor='grey',
                                          fill=True,
                                          lw=1))
        if self.over:
            fx, tx = self.axes.get_xlim()
            fy, ty = self.axes.get_ylim()
            w, h = tx - fx, ty - fy
            x, y = w / 2, h / 2
            window_width = 8
            window_height = 4
            self.axes.add_patch(Rectangle((x - window_width / 2, y - window_height / 2), window_width, window_height,
                                          facecolor='grey',
                                          edgecolor='white',
                                          fill=True,
                                          alpha=0.5,
                                          lw=1))
            font_color = 'black'
            self.axes.text(x, y, 'Game Over', ha='center', va='center', fontsize='20', color=font_color, fontweight='bold')
            self.axes.text(x, y - 1, 'Press Enter To Restart', ha='center', va='center', fontsize='10', color=font_color, fontweight='bold')

    def after_down(self):
        obj = find_object(self.map)
        for x, y in obj:
            self.map[x][y] = 1
        self.map = disappear(self.map)

    def beep(self):
        pass

    def on_cmd(self, cmd: int):
        cmd = cmd.key
        if cmd == -1:
            return
        if self.over:
            if cmd == 'enter':
                self.init(self.rows, self.cols)
            return
        obj = find_object(self.map)
        log.info(f"got command {cmd}")
        if not obj:
            log.info(f" no object can be found")
            return
        if cmd == "right":
            if not move(obj, 0, 1, self.map):
                self.beep()
        elif cmd == "left":
            if not move(obj, 0, -1, self.map):
                self.beep()
        elif cmd == "up":
            if not rotate(obj, self.map):
                self.beep()
        elif cmd == "down":
            while move(obj, 1, 0, self.map):
                obj = find_object(self.map)
            self.after_down()

    def init(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.over = False
        self.tick = 0  # 始终tick，每隔多少个时钟走一格
        self.map = np.zeros((self.rows, self.cols), dtype=np.int)

    def main(self):
        rows, cols = 20, 10
        self.init(rows, cols)
        fig_height = 8
        fig, self.axes = plt.subplots(figsize=(fig_height / rows * cols, fig_height), )
        # fig, self.axes = plt.subplots(figsize=(fig_height / rows * cols, fig_height), facecolor='black')
        fig.canvas.mpl_connect('key_press_event', self.on_cmd)
        _ = animation.FuncAnimation(fig, self.update, interval=200)
        plt.show()


Teris().main()
