# Create a bar plot.
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.bar([1, 2, 3], [2, 1, 3])
chart.show()
#
# Hide it.
#
plot.visible = False
chart.show()
