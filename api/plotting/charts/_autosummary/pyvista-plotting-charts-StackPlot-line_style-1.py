# Set a custom line style.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.stack([0, 1, 2], [2, 1, 3])
plot.line_style = '-.'
chart.show()
