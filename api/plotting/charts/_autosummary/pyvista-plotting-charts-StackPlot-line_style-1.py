# Set a custom line style.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.stack([0, 1, 2], [2, 1, 3])
plot.line_style = '-.'
chart.show()
