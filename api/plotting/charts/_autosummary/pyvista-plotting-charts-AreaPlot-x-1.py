# Create an area plot and display the x coordinates.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.area([0, 1, 2], [2, 1, 3], [1, 0, 1])
plot.x
# Expected:
## pyvista_ndarray([0, 1, 2])
chart.show()
