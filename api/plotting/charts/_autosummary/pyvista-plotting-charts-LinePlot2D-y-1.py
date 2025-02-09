# Create a line plot and display the y coordinates.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.line([0, 1, 2], [2, 1, 3])
plot.y
# Expected:
## pyvista_ndarray([2, 1, 3])
chart.show()
