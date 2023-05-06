# Set a custom line style.
#
import pyvista
chart = pyvista.ChartPie([4, 3, 2, 1])
plot = chart.plot
plot.line_style = '-.'
chart.show()
