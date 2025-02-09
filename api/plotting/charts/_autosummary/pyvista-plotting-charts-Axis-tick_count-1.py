# Create a 2D chart with a reduced number of ticks on the x-axis.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.Chart2D()
_ = chart.line([0, 1, 2], [2, 1, 3])
chart.x_axis.tick_count = 5
chart.show()
#
#    Revert back to automatic tick behavior.
#
chart.x_axis.tick_count = None
chart.show()
