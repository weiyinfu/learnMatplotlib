import numpy as np
from bokeh.plotting import figure, output_file, show

x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)
# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(x, np.sin(x), legend_label="sin", line_width=2)
p.line(x, np.cos(x), legend_label="cos", line_width=2)
show(p)
