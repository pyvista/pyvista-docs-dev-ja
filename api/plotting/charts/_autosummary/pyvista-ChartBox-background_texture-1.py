# Create a boxplot chart with an emoji as its background.
#
import pyvista
from pyvista import examples
chart = pyvista.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
chart.background_texture = examples.download_emoji_texture()
chart.show(interactive=False)
