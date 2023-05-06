# Create a 2D chart with an emoji as its background.
#
import pyvista
from pyvista import examples
chart = pyvista.Chart2D()
plot = chart.line([0, 1, 2], [2, 1, 3])
chart.background_texture = examples.download_emoji_texture()
chart.show(interactive=False)
