# Create a 2D chart with no visible y-axis.
#
import pyvista
chart = pyvista.Chart2D()
_ = chart.line([0, 1, 2], [2, 1, 3])
chart.y_axis.visible = False
chart.show()
