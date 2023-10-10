# Create a line plot.
#
import pyvista as pv
chart = pv.Chart2D()
plot = chart.line([0, 1, 2], [2, 1, 3])
chart.show()
#
# Update the line's y coordinates.
#
plot.update([0, 1, 2], [3, 1, 2])
chart.show()
