# Set the stack plot's color to red.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.stack([0, 1, 2], [2, 1, 3])
plot.color = 'r'
chart.show()
