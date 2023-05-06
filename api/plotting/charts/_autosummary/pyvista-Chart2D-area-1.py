# Generate an area plot.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.area([0, 1, 2], [2, 1, 3])
chart.show()
