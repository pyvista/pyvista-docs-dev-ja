# Add two meshes to a plotter and then remove the sphere actor.
#
import pyvista as pv
mesh = pv.Cube()
pl = pv.Plotter()
cube_actor = pl.add_mesh(pv.Cube(), show_edges=True)
sphere_actor = pl.add_mesh(pv.Sphere(), show_edges=True)
_ = pl.remove_actor(cube_actor)
pl.show()
