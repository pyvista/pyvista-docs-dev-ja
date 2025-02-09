# Set the x-axis label font size of a 2D chart to 20.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.Chart2D()
_ = chart.line([0, 1, 2], [2, 1, 3])
chart.x_axis.label_size = 20
chart.x_axis.label_size
# Expected:
## 20
chart.show()
