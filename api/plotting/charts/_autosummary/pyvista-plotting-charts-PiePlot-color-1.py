# Set the pie plot's color to red.
#
import pyvista as pv
chart = pv.ChartPie([4, 3, 2, 1])
plot = chart.plot
plot.color = 'r'
chart.show()
