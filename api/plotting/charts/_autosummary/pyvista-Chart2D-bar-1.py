# Generate a bar plot.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.bar([0, 1, 2], [2, 1, 3])
chart.show()
