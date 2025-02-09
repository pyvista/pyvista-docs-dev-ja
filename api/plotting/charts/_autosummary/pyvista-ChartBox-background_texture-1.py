# Create a boxplot chart with an emoji as its background.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
from pyvista import examples
chart = pv.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
chart.background_texture = examples.download_emoji_texture()
chart.show(interactive=False)
