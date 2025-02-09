# Set the stack plot's colors manually.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.stack([0, 1, 2], [[2, 1, 3], [1, 0, 2], [0, 3, 1], [3, 2, 0]])
plot.colors = ['b', 'g', 'r', 'c']
chart.show()
