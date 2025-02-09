# Plot a simple sine wave as a scatter plot.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
import numpy as np
x = np.linspace(0, 2 * np.pi, 20)
y = np.sin(x)
chart = pv.Chart2D()
_ = chart.scatter(x, y)
chart.show()
