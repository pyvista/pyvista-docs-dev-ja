# Create a 2D chart.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.Chart2D()
_ = chart.line([0, 1, 2], [2, 1, 3])
chart.show()
#
#    Toggle the visibility of the y-axis.
#
chart.y_axis.toggle()
chart.show()
