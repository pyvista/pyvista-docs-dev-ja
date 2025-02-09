import pyvista as pv
import numpy as np
x = np.linspace(0, 2 * np.pi, 20)
y = np.sin(x)
chart = pv.Chart2D()
_ = chart.line(x, y, 'r')
chart.grid = False
chart.show()
#
# Enable the grid
#
chart.grid = True
chart.show()
