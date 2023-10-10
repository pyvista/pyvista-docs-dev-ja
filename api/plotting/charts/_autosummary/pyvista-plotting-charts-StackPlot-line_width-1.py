# Set the line width to 10
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.stack([0, 1, 2], [2, 1, 3])
plot.line_style = '-'  # Make sure all lines are visible
plot.line_width = 10
chart.show()
