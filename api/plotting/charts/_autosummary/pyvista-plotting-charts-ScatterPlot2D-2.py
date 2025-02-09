import pyvista as pv
import numpy as np
x = np.linspace(0, 2 * np.pi, 20)
y = np.sin(x)
chart = pv.Chart2D()
_ = chart.scatter(x, y)
chart.show()
