# Create a half-sized pie chart centered in the middle of the
# renderer.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.ChartPie([5, 4, 3, 2, 1])
chart.size = (0.5, 0.5)
chart.loc = (0.25, 0.25)
chart.show()
