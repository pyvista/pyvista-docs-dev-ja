# Increase the line width of the bar plot's pen object.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.bar([1, 2, 3], [2, 1, 3])
plot.line_style = '-'  # Make sure all lines are visible
plot.pen.width = 10
chart.show()
