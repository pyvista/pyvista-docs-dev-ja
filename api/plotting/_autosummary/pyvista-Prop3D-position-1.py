# Change the position of an actor. Note how this does not change the
# position of the underlying dataset, just the relative location of the
# actor in the :class:`pyvista.Plotter`.
#
import pyvista as pv
mesh = pv.Sphere()
pl = pv.Plotter()
_ = pl.add_mesh(mesh, color='b')
actor = pl.add_mesh(mesh, color='r')
actor.position = (0, 0, 1)  # shifts the red sphere up
pl.show()
