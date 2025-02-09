# Create a scatter plot and display the x coordinates.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.scatter([0, 1, 2, 3, 4], [2, 1, 3, 4, 2])
plot.x
# Expected:
## pyvista_ndarray([0, 1, 2, 3, 4])
chart.show()
