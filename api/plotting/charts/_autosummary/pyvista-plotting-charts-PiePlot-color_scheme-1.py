# Set the pie plot's color scheme to warm.
#
import pyvista
chart = pyvista.ChartPie([4, 3, 2, 1])
plot = chart.plot
plot.color_scheme = "warm"
chart.show()
