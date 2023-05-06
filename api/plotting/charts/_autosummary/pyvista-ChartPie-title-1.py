# Create a pie chart with title 'My Chart'.
#
import pyvista
chart = pyvista.ChartPie([5, 4, 3, 2, 1])
chart.title = 'My Chart'
chart.show()
