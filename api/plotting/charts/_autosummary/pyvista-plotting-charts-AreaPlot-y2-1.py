# Create an area plot and display the y2 coordinates.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.area([0, 1, 2], [2, 1, 3], [1, 0, 1])
plot.y2
# Expected:
## pyvista_ndarray([1, 0, 1])
chart.show()
