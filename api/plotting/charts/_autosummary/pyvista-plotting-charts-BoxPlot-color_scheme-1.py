# Set the box plot's color scheme to warm.
#
import pyvista
chart = pyvista.ChartBox([[0, 1, 1, 2, 3, 4, 5], [0, 1, 2, 2, 3, 4, 5], [0, 1, 2, 3, 3, 4, 5], [0, 1, 2, 3, 4, 4, 5]])
plot = chart.plot
plot.color_scheme = "warm"
chart.show()
