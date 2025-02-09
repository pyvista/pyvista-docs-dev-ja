# Use a custom texture for the pie plot's brush object.
#
# .. pyvista-plot::
#    :force_static:
#
import pyvista as pv
from pyvista import examples
chart = pv.ChartPie([4, 3, 2, 1])
plot = chart.plot
plot.brush.texture = examples.download_puppy_texture()
chart.show()
