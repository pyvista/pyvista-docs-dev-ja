# Create a pie plot with custom label.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
import numpy as np
chart = pv.ChartPie([4, 3, 2, 1])
plot = chart.plot
chart.show()
#
#    Modify the label.
#
plot.label = 'My awesome plot'
chart.show()
