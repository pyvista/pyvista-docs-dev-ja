# Create an actor and add a texture to it. Note how the
# :class:`pyvista.PolyData` has texture coordinates by default.
#
import pyvista as pv
from pyvista import examples
plane = pv.Plane()
plane.active_t_coords is not None
# Expected:
## True
pl = pv.Plotter()
actor = pl.add_mesh(plane)
actor.texture = examples.download_masonry_texture()
actor.texture  # doctest:+SKIP
# Expected:
## <Texture(0x378c920) at 0x7f7af577e700>
