# Set the axis label to ``"Axis Label"``.
#
import pyvista
chart = pyvista.Chart2D()
_ = chart.line([0, 1, 2], [2, 1, 3])
chart.x_axis.label = "Axis Label"
chart.show()
