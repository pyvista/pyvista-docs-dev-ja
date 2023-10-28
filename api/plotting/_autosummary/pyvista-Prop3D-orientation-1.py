# Reorient just the actor and plot it. Note how the actor is rotated
# about its own axes as defined by its position.
#
import pyvista as pv
mesh = pv.Cube()
pl = pv.Plotter()
_ = pl.add_mesh(mesh, color='b')
actor = pl.add_mesh(
    mesh,
    color='r',
    style='wireframe',
    line_width=5,
    lighting=False,
)
actor.position = (0, 0, 1)
actor.orientation = (45, 0, 0)
pl.show_axes()
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
