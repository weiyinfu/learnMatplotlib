matplotlib提供了丰富的实例，但是这些实例年久失修，有些不能用了。

https://matplotlib.org/gallery/index.html

matplotlib比从头写可视化程序简单多了。

任何一个库仔细探索都是无底洞，而常用的却是很少的一部分。

# pylab
pylab是matplotlib的入口文件之一，它是一大堆import的集合，用途就是便于用户只import一个文件就能够获取大量的便捷函数。  

# 两类画图方式
matplotlib画出来的是原生图像，seaborn是基于matplotlib的，它把matplotlib视作汇编语言。  
bokeh、plotly是基于HTML的交互式画图，echarts、d3等也是基于前端的画图。这种方式在丰富性、交互性方面完胜原生图像。    
以上是两类画图方式。  
在实践中，如果数据量巨大，HTML画图是必不可少的。如果只是简单的画图，使用matplotlib具有简单便捷的特点。    

# Python画图库
* Matplotlib：静态图
* Seaborn：基于matplotlib进行封装
* Plotly：收费版
* Echarts：pyecharts是对echarts的封装，最终会生成html文件。
* bokeh：html画图

# 词汇
Contours Line：等高线
pie：饼图
polar：极坐标系

# 部分实例需要安装ffmpeg

# skimage+mapplotlib的imshow实现游戏画图