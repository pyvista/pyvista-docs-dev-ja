# Create a box plot.
#
import pyvista
chart = pyvista.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
plot = chart.plot
chart.show()
#
# Hide it.
#
plot.visible = False
chart.show()
