# Create a 2D chart with hidden ticks on the y-axis.
#
import pyvista
chart = pyvista.Chart2D()
_ = chart.line([0, 1, 2], [2, 1, 3])
chart.y_axis.ticks_visible = False
chart.show()
