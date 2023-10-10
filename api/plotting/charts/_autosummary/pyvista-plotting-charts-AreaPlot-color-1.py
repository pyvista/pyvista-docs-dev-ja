# Set the area plot's color to red.
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.area([0, 1, 2], [0, 0, 1], [1, 3, 2])
plot.color = 'r'
chart.show()
