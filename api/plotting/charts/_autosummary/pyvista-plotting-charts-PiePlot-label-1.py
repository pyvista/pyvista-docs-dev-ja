# Create a pie plot with custom label.
#
import pyvista
import numpy as np
chart = pyvista.ChartPie([4, 3, 2, 1])
plot = chart.plot
chart.show()
#
# Modify the label.
#
plot.label = "My awesome plot"
chart.show()
