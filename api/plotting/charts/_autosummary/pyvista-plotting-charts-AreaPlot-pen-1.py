# Increase the line width of the area plot's pen object.
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.area([0, 1, 2], [0, 0, 1], [1, 3, 2])
plot.line_style = '-'  # Make sure all lines are visible
plot.pen.width = 10
chart.show()
