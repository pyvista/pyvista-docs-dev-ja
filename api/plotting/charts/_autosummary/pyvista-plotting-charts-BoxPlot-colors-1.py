# Set the box plot's colors manually.
#
import pyvista
chart = pyvista.ChartBox([[0, 1, 1, 2, 3, 4, 5], [0, 1, 2, 2, 3, 4, 5], [0, 1, 2, 3, 3, 4, 5], [0, 1, 2, 3, 4, 4, 5]])
plot = chart.plot
plot.colors = ["b", "g", "r", "c"]
chart.show()
