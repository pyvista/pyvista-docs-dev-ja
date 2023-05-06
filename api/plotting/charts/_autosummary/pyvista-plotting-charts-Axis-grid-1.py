# Create a 2D chart with grid lines disabled for the x-axis.
#
import pyvista
chart = pyvista.Chart2D()
_ = chart.line([0, 1, 2], [2, 1, 3])
chart.x_axis.grid = False
chart.show()
