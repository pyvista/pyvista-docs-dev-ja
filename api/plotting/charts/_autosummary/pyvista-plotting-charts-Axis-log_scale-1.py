# Create a 2D chart.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.Chart2D()
_ = chart.line([0, 1, 2, 3, 4], [1e0, 1e1, 1e2, 1e3, 1e4])
chart.show()
#
#    Try to enable the log scale on the y-axis.
#
chart.y_axis.log_scale = True
chart.show()
chart.y_axis.log_scale
# Expected:
## True
