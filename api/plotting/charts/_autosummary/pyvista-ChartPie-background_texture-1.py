# Create a pie chart with an emoji as its background.
#
import pyvista
from pyvista import examples
chart = pyvista.ChartPie([5, 4, 3, 2, 1])
chart.background_texture = examples.download_emoji_texture()
chart.show(interactive=False)
