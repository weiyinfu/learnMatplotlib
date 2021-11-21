"""
cbook即为cookbook，是一些小工具组成的库

"""
from matplotlib.cbook import CallbackRegistry

callbacks = CallbackRegistry()
sum = lambda x, y: print(f'{x}+{y}={x + y}')
mul = lambda x, y: print(f"{x} * {y}={x * y}")
id_sum = callbacks.connect("sum", sum)
id_mul = callbacks.connect("mul", mul)
callbacks.process('sum', 3, 4)
callbacks.process("mul", 5, 6)
callbacks.disconnect(id_sum)
callbacks.process("sum", 7, 8)
