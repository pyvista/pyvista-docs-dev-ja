# Set the pie plot's colors manually.
#
import pyvista
chart = pyvista.ChartPie([4, 3, 2, 1])
plot = chart.plot
plot.colors = ["b", "g", "r", "c"]
chart.show()
