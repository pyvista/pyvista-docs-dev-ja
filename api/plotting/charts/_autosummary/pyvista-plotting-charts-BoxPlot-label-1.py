# Create a box plot with custom label.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
import numpy as np
chart = pv.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
plot = chart.plot
chart.show()
#
#    Modify the label.
#
plot.label = 'My awesome plot'
chart.show()
