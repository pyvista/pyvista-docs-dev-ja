# Create a 2D chart with the grid disabled.
#
import pyvista
import numpy as np
x = np.linspace(0, 2*np.pi, 20)
y = np.sin(x)
chart = pyvista.Chart2D()
_ = chart.line(x, y, 'r')
chart.grid = False
chart.show()
#
# Enable the grid
#
chart.grid = True
chart.show()
