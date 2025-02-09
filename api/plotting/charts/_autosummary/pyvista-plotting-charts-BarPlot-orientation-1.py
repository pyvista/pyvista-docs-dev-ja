# Create a bar plot.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.bar([1, 2, 3], [[2, 1, 3], [1, 3, 2]])
chart.show()
#
#    Change the orientation to horizontal.
#
plot.orientation = 'H'
chart.show()
