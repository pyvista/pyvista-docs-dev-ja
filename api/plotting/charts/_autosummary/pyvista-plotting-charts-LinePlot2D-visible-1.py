# Create a 2D line plot.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.line([0, 1, 2], [2, 1, 3])
chart.show()
#
# Hide it.
#
plot.visible = False
chart.show()
