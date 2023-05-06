# Create a 3D plotter and add a CubeAxesActor to it.
#
import pyvista as pv
mesh = pv.Cube()
pl = pv.Plotter()
actor = pl.add_mesh(mesh)
cube_axes_actor = pv.CubeAxesActor(pl.camera)
cube_axes_actor.bounds = mesh.bounds
actor, property = pl.add_actor(cube_axes_actor)
pl.show()
