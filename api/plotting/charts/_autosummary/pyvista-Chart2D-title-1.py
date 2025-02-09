# Create a 2D chart with title 'My Chart'.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.line([0, 1, 2], [2, 1, 3])
chart.title = 'My Chart'
chart.show()
