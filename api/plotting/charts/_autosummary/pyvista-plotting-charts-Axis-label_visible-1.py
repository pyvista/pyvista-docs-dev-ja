# Hide the x-axis label of a 2D chart.
#
import pyvista
chart = pyvista.Chart2D()
_ = chart.line([0, 1, 2], [2, 1, 3])
chart.x_axis.label_visible = False
chart.show()
