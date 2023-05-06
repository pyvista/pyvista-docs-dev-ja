# Create a 2D chart with title 'My Chart'.
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.line([0, 1, 2], [2, 1, 3])
chart.title = 'My Chart'
chart.show()
