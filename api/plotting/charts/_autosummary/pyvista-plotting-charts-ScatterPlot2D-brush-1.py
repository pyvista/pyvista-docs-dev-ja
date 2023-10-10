# Use a custom texture for the 2D scatter plot's brush object.
#
import pyvista as pv
from pyvista import examples
chart = pv.Chart2D()
plot = chart.scatter([0, 1, 2, 3, 4], [2, 1, 3, 4, 2])
plot.brush.texture = examples.download_puppy_texture()
chart.show()
