# Set a custom line style.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.bar([1, 2, 3], [2, 1, 3])
plot.line_style = '-.'
chart.show()
