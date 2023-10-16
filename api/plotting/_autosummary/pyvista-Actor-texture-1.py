# Create an actor and add a texture to it. Note how the
# :class:`pyvista.PolyData` has texture coordinates by default.
#
import pyvista as pv
from pyvista import examples
plane = pv.Plane()
plane.active_texture_coordinates is not None
# Expected:
## True
pl = pv.Plotter()
actor = pl.add_mesh(plane)
actor.texture = examples.download_masonry_texture()
actor.texture
# Expected:
## Texture (...)
##   Components:   3
##   Cube Map:     False
##   Dimensions:   256, 256
