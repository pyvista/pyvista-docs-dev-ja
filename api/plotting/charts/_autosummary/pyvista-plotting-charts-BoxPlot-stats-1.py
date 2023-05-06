# Create a box plot and display the statistics.
#
import pyvista
chart = pyvista.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
chart.plot.stats
# Expected:
## (pyvista_ndarray([0., 1., 2., 3., 4.]),)
chart.show()
