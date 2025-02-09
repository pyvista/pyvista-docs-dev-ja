# Reorient just the actor and plot it. Note how the actor is rotated
# about the origin ``(0, 0, 0)`` by default.
#
import pyvista as pv
mesh = pv.Cube(center=(0, 0, 3))
pl = pv.Plotter()
_ = pl.add_mesh(mesh, color='b')
actor = pl.add_mesh(
    mesh,
    color='r',
    style='wireframe',
    line_width=5,
    lighting=False,
)
actor.orientation = (45, 0, 0)
_ = pl.add_axes_at_origin()
pl.show()
#
# Repeat the last example, but this time reorient the actor about
# its center by specifying its :attr:`~origin`.
#
import pyvista as pv
mesh = pv.Cube(center=(0, 0, 3))
pl = pv.Plotter()
_ = pl.add_mesh(mesh, color='b')
actor = pl.add_mesh(
    mesh,
    color='r',
    style='wireframe',
    line_width=5,
    lighting=False,
)
actor.origin = actor.center
actor.orientation = (45, 0, 0)
_ = pl.add_axes_at_origin()
pl.show()
#
# Show that the orientation changes with rotation.
#
import pyvista as pv
mesh = pv.Cube()
pl = pv.Plotter()
actor = pl.add_mesh(mesh)
actor.rotate_x(90)
actor.orientation  # doctest:+SKIP
# Expected:
## (90, 0, 0)
#
# Set the orientation directly.
#
actor.orientation = (0, 45, 45)
actor.orientation  # doctest:+SKIP
# Expected:
## (0, 45, 45)
