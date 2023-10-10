# Create a stack plot and display the sizes.
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.stack([0, 1, 2], [[2, 1, 3], [1, 2, 0]])
plot.ys
# Expected:
## (pyvista_ndarray([2, 1, 3]), pyvista_ndarray([1, 2, 0]))
chart.show()
