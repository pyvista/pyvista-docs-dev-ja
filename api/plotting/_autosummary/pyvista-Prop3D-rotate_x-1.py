# Rotate the actor about the x-axis 45 degrees. Note how this does not
# change the location of the underlying dataset.
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
actor.rotate_x(45)
pl.show_axes()
pl.show()
