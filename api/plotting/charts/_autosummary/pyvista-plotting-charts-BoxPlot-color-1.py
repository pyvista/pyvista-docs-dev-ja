# Set the box plot's color to red.
#
import pyvista
chart = pyvista.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
plot = chart.plot
plot.color = 'r'
chart.show()
