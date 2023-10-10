# Create a area plot.
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.area([0, 1, 2], [0, 0, 1], [1, 3, 2])
chart.show()
#
# Hide it.
#
plot.visible = False
chart.show()
