import pyvista as pv
from pyvista import examples
chart = pv.Chart2D()
plot = chart.line([0, 1, 2], [2, 1, 3])
chart.background_texture = examples.download_emoji_texture()
chart.show(interactive=False)
