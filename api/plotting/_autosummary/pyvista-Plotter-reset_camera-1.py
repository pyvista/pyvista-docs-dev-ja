# Add a mesh and place the camera position too close to the
# mesh.  Then reset the camera and show the mesh.
#
import pyvista as pv
pl = pv.Plotter()
actor = pl.add_mesh(pv.Sphere(), show_edges=True)
pl.set_position((0, 0.1, 0.1))
pl.reset_camera()
pl.show()
