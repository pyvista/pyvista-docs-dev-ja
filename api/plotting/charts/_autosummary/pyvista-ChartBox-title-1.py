# Create a boxplot chart with title 'My Chart'.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
chart.title = 'My Chart'
chart.show()
