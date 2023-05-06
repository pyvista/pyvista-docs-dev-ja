# Create a pie plot.
#
import pyvista
chart = pyvista.ChartPie([4, 3, 2, 1])
plot = chart.plot
chart.show()
#
# Hide it.
#
plot.toggle()
chart.show()
