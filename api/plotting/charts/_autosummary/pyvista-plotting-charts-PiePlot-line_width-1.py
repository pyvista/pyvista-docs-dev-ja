# Set the line width to 10
#
import pyvista
chart = pyvista.ChartPie([4, 3, 2, 1])
plot = chart.plot
plot.line_style = '-'  # Make sure all lines are visible
plot.line_width = 10
chart.show()
