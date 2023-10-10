# Create a 2D plot and set custom axis labels.
#
import pyvista as pv
chart = pv.Chart2D()
_ = chart.line([0, 1, 2], [2, 1, 3])
chart.x_label = "Horizontal axis"
chart.y_label = "Vertical axis"
chart.show()
