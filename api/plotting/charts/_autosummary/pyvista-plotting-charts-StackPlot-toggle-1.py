# Create a stack plot.
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.stack([0, 1, 2], [2, 1, 3])
chart.show()
#
# Hide it.
#
plot.toggle()
chart.show()
