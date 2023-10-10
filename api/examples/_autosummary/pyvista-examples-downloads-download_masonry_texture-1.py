# Create plot the masonry testure on a surface.
#
import pyvista as pv
from pyvista import examples
texture = examples.download_masonry_texture()
surf = pv.Cylinder()
surf.plot(texture=texture)
#
# See :ref:`texture_example` for an example using this
