# Create a box plot and display the statistics.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
chart.plot.stats
# Expected:
## (pyvista_ndarray([0., 1., 2., 3., 4.]),)
chart.show()
