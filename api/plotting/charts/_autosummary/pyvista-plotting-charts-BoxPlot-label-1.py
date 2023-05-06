# Create a box plot with custom label.
#
import pyvista
import numpy as np
chart = pyvista.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
plot = chart.plot
chart.show()
#
# Modify the label.
#
plot.label = "My awesome plot"
chart.show()
