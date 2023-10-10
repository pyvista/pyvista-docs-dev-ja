# Shows an interactive plane used to clip the mesh and store it.
#
import pyvista as pv
from pyvista import examples
vol = examples.load_airplane()
pl = pv.Plotter()
_ = pl.add_mesh_clip_plane(vol, normal=[0, -1, 0])
pl.show(cpos=[-2.1, 0.6, 1.5])
pl.plane_clipped_meshes  # doctest:+SKIP
