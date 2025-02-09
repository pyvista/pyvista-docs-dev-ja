# Set the pie plot's color scheme to warm.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.ChartPie([4, 3, 2, 1])
plot = chart.plot
plot.color_scheme = 'warm'
chart.show()
