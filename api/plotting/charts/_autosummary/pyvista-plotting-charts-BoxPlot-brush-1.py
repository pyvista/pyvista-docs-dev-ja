# Use a custom texture for the box plot's brush object.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
from pyvista import examples
chart = pv.ChartBox([[0, 1, 1, 2, 3, 3, 4]])
plot = chart.plot
plot.brush.texture = examples.download_puppy_texture()
chart.show()
