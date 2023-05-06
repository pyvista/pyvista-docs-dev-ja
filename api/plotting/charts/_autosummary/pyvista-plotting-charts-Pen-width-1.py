# Set the pen's width to 10
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.line([0, 1, 2], [2, 1, 3])
plot.pen.width = 10
chart.show()
