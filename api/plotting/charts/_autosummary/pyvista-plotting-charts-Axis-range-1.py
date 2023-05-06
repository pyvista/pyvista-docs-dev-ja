# Manually specify the x-axis range of a 2D chart.
#
import pyvista
chart = pyvista.Chart2D()
_ = chart.line([0, 1, 2], [2, 1, 3])
chart.x_axis.range = [0, 5]
chart.show()
#
# Revert to automatic axis scaling.
#
chart.x_axis.range = None
chart.show()
