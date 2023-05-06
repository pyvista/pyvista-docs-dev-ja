# Create a bar plot and display the sizes.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.bar([1, 2, 3], [[2, 1, 3], [1, 2, 0]])
plot.y
# Expected:
## (pyvista_ndarray([2, 1, 3]), pyvista_ndarray([1, 2, 0]))
chart.show()
