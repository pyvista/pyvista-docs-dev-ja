# Create an area plot.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.area([0, 1, 2], [2, 1, 3])
chart.show()
#
# Update the points on the second outline of the area.
#
plot.update([0, 1, 2], [2, 1, 3], [1, 0, 1])
chart.show()
