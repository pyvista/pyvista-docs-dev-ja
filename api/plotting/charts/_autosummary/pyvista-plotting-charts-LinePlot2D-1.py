# Create a 2D chart plotting an approximate satellite
# trajectory.
#
import pyvista
from pyvista import examples
import numpy as np
chart = pyvista.Chart2D()
x = np.linspace(0, 1, 100)
y = np.sin(6.5*x-1)
_ = chart.line(x, y, "y", 4)
chart.background_texture = examples.load_globe_texture()
chart.hide_axes()
chart.show()
