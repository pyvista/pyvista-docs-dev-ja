# Create an actor using the :class:`pyvista.Plotter` and then change the
# visibility of the actor.
#
import pyvista as pv
pl = pv.Plotter()
actor = pl.add_mesh(pv.Sphere())
actor.visibility = False
actor.visibility
# Expected:
## False
