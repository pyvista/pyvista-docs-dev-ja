# Create a scatter plot and display the x coordinates.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.scatter([0, 1, 2, 3, 4], [2, 1, 3, 4, 2])
plot.x
# Expected:
## pyvista_ndarray([0, 1, 2, 3, 4])
chart.show()
