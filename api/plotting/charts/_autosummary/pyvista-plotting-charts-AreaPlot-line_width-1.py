# Set the line width to 10
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.area([0, 1, 2], [0, 0, 1], [1, 3, 2])
plot.line_style = '-'  # Make sure all lines are visible
plot.line_width = 10
chart.show()
