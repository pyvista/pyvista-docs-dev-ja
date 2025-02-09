# Apply a 4x4 translation to a wireframe actor. This 4x4 transformation
# effectively translates the actor by one unit in the Z direction,
# rotates the actor about the z-axis by approximately 45 degrees, and
# shrinks the actor by a factor of 0.5.
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
arr = [
    [0.707, -0.707, 0, 0],
    [0.707, 0.707, 0, 0],
    [0, 0, 1, 1.5],
    [0, 0, 0, 2],
]
actor.user_matrix = arr
pl.show_axes()
pl.show()
