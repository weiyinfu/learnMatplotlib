from matplotlib.cbook import Grouper

"""
Grouper是一个类似并查集的结构，它能够判断两个结点之间是否可达
"""


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


a, b, c, d, e = list(map(Person, list("abcde")))
g = Grouper()
g.join(a, b)
g.join(b, c)
g.join(d, e)
print(list(map(tuple, g)))
print(g.joined(a, c))
print(g.joined(a, b))
print(g.joined(a, d))
