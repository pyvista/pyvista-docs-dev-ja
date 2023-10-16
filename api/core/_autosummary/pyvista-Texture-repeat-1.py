# Load the masonry texture and create a simple :class:`pyvista.PolyData`
# with texture coordinates using :func:`pyvista.Plane`. By default the
# texture coordinates are between 0 and 1. Let's raise these values over
# 1 by multiplying them in place. This will allow us to wrap the texture.
#
import pyvista as pv
from pyvista import examples
texture = examples.download_masonry_texture()
plane = pv.Plane()
plane.active_texture_coordinates *= 2
#
# This is the texture plotted with repeat set to ``False``.
#
texture.repeat = False
pl = pv.Plotter()
actor = pl.add_mesh(plane, texture=texture)
pl.camera.zoom('tight')
pl.show()
#
# This is the texture plotted with repeat set to ``True``.
#
texture.repeat = True
pl = pv.Plotter()
actor = pl.add_mesh(plane, texture=texture)
pl.camera.zoom('tight')
pl.show()
