from bokeh.plotting import figure
from bokeh.plotting import output_file
from bokeh.plotting import show

import numpy as np
import math

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(title = "simple line example", x_axis_label = 'x', y_axis_label = 'y')
p.line(x, y, legend_label = "Temp", line_width = 2)

#output_file("Test_graph.html")
show(p)