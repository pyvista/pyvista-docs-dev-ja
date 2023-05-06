# Set the line width to 10
#
import pyvista
chart = pyvista.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
plot = chart.plot
plot.line_style = '-'  # Make sure all lines are visible
plot.line_width = 10
chart.show()
