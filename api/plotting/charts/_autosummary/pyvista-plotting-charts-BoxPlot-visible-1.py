# Create a box plot.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
plot = chart.plot
chart.show()
#
#    Hide it.
#
plot.visible = False
chart.show()
