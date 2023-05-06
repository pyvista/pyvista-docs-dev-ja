# Set a custom line style.
#
import pyvista
chart = pyvista.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
plot = chart.plot
plot.line_style = '-.'
chart.show()
