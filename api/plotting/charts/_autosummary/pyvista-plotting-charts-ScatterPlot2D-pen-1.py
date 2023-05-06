# Increase the line width of the 2D scatter plot's pen object.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.scatter([0, 1, 2, 3, 4], [2, 1, 3, 4, 2])
plot.line_style = '-'  # Make sure all lines are visible
plot.pen.width = 10
chart.show()
