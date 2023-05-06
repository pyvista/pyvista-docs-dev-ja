# Generate a bar plot.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.bar([0, 1, 2], [2, 1, 3])
chart.show()
