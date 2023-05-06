# Generate a scatter plot.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.scatter([0, 1, 2], [2, 1, 3])
chart.show()
