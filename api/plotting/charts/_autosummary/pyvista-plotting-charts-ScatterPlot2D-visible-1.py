# Create a 2D scatter plot.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.scatter([0, 1, 2, 3, 4], [2, 1, 3, 4, 2])
chart.show()
#
# Hide it.
#
plot.visible = False
chart.show()
