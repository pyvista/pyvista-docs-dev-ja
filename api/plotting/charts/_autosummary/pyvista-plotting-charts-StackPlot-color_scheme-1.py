# Set the stack plot's color scheme to warm.
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.stack([0, 1, 2], [[2, 1, 3], [1, 0, 2], [0, 3, 1], [3, 2, 0]])
plot.color_scheme = "warm"
chart.show()
