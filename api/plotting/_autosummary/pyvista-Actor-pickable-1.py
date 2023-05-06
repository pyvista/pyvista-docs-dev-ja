# Create an actor using the :class:`pyvista.Plotter` and then make the
# actor unpickable.
#
import pyvista as pv
pl = pv.Plotter()
actor = pl.add_mesh(pv.Sphere())
actor.pickable = False
actor.pickable
# Expected:
## False
