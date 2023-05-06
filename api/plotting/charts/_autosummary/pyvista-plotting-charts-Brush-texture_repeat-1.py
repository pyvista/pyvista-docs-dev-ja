# Set up a brush with a texture.
#
import pyvista
from pyvista import examples
chart = pyvista.Chart2D()
plot = chart.area([0, 1, 2], [0, 0, 1], [1, 3, 2])
plot.brush.texture = examples.download_puppy_texture()
chart.show()
#
# Enable texture repeat.
#
plot.brush.texture_repeat = True
chart.show()
