# Create a simple 2D chart and show it.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.line([0, 1, 2], [2, 1, 3])
chart.show()
