# Create a scatter plot.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.scatter([0, 1, 2, 3, 4], [2, 1, 3, 4, 2])
chart.show()
#
# Update the marker locations.
#
plot.update([0, 1, 2, 3, 4], [3, 2, 4, 2, 1])
chart.show()
