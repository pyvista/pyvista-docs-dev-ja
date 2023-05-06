# Set the line width to 10
#
import pyvista
chart = pyvista.Chart2D()
plot = chart.line([0, 1, 2], [2, 1, 3])
plot.line_style = '-'  # Make sure all lines are visible
plot.line_width = 10
chart.show()
