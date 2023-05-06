# Create plot the masonry testure on a surface.
#
import pyvista
from pyvista import examples
texture = examples.download_masonry_texture()
surf = pyvista.Cylinder()
surf.plot(texture=texture)
#
# See :ref:`ref_texture_example` for an example using this
