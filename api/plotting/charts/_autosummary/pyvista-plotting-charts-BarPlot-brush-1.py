# Use a custom texture for the bar plot's brush object.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
from pyvista import examples
chart = pv.Chart2D()
plot = chart.bar([1, 2, 3], [2, 1, 3])
plot.brush.texture = examples.download_puppy_texture()
chart.show()
