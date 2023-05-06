# Add two actors to a :class:`pyvista.Plotter`, make one
# pickable, and then list the pickable actors.
#
import pyvista as pv
pl = pv.Plotter()
sphere_actor = pl.add_mesh(pv.Sphere())
cube_actor = pl.add_mesh(
    pv.Cube(), pickable=False, style='wireframe'
)
len(pl.pickable_actors)
# Expected:
## 1
#
# Set the pickable actors to both actors.
#
pl.pickable_actors = [sphere_actor, cube_actor]
len(pl.pickable_actors)
# Expected:
## 2
#
# Set the pickable actors to ``None``.
#
pl.pickable_actors = None
len(pl.pickable_actors)
# Expected:
## 0
