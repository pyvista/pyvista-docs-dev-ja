# Generate a stack plot.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.stack([0, 1, 2], [[2, 1, 3],[1, 2, 1]])
chart.show()
