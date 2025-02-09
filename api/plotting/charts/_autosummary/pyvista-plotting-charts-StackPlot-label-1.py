# Create a stack plot with custom label.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
import numpy as np
chart = pv.Chart2D()
plot = chart.stack([0, 1, 2], [2, 1, 3])
chart.show()
#
#    Modify the label.
#
plot.label = 'My awesome plot'
chart.show()
