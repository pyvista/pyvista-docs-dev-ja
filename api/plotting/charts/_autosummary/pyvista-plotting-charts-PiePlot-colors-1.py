# Set the pie plot's colors manually.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.ChartPie([4, 3, 2, 1])
plot = chart.plot
plot.colors = ['b', 'g', 'r', 'c']
chart.show()
