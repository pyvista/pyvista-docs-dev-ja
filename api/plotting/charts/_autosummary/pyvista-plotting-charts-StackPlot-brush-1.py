# Use a custom texture for the stack plot's brush object.
#
import pyvista as pv
from pyvista import examples
chart = pv.Chart2D()
plot = chart.stack([0, 1, 2], [2, 1, 3])
plot.brush.texture = examples.download_puppy_texture()
chart.show()
