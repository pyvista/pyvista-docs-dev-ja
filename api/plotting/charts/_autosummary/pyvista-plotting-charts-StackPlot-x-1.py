# Create a stack plot and display the x coordinates.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.stack([0, 1, 2], [[2, 1, 3], [1, 2, 0]])
plot.x
# Expected:
## pyvista_ndarray([0, 1, 2])
chart.show()
