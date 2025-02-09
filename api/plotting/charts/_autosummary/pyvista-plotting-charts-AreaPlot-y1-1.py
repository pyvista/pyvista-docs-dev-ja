# Create an area plot and display the y1 coordinates.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.area([0, 1, 2], [2, 1, 3], [1, 0, 1])
plot.y1
# Expected:
## pyvista_ndarray([2, 1, 3])
chart.show()
