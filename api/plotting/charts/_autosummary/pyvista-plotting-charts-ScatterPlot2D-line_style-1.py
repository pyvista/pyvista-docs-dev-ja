# Set a custom line style.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.scatter([0, 1, 2, 3, 4], [2, 1, 3, 4, 2])
plot.line_style = '-.'
chart.show()
