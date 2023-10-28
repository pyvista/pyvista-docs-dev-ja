# Create an actor using the :class:`pyvista.Plotter` and then change the
# scale of the actor.
#
import pyvista as pv
pl = pv.Plotter()
actor = pl.add_mesh(pv.Sphere())
actor.scale = (2.0, 2.0, 2.0)
actor.scale
# Expected:
## (2.0, 2.0, 2.0)
