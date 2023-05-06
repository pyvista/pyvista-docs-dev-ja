# Increase the line width of the box plot's pen object.
#
import pyvista
chart = pyvista.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
plot = chart.plot
plot.line_style = '-'  # Make sure all lines are visible
plot.pen.width = 10
chart.show()
