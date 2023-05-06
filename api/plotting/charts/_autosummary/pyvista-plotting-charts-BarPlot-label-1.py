# Create a bar plot with custom label.
#
import pyvista
import numpy as np
chart = pyvista.Chart2D()
plot = chart.bar([1, 2, 3], [2, 1, 3])
chart.show()
#
# Modify the label.
#
plot.label = "My awesome plot"
chart.show()
