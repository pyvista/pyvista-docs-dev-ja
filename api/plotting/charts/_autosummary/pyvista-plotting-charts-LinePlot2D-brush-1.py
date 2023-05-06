# Use a custom texture for the 2D line plot's brush object.
#
import pyvista
from pyvista import examples
chart = pyvista.Chart2D()
plot = chart.line([0, 1, 2], [2, 1, 3])
plot.brush.texture = examples.download_puppy_texture()
chart.show()
