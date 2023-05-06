# Plot a simple sine wave as a scatter plot.
#
import pyvista
import numpy as np
x = np.linspace(0, 2*np.pi, 20)
y = np.sin(x)
chart = pyvista.Chart2D()
_ = chart.scatter(x, y)
chart.show()
