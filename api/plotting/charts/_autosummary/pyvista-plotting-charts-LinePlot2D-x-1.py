# Create a line plot and display the x coordinates.
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.line([0, 1, 2], [2, 1, 3])
plot.x
# Expected:
## pyvista_ndarray([0, 1, 2])
chart.show()
