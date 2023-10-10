# Increase the line width of the stack plot's pen object.
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.stack([0, 1, 2], [2, 1, 3])
plot.line_style = '-'  # Make sure all lines are visible
plot.pen.width = 10
chart.show()
