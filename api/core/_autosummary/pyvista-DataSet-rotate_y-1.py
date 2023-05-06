# Rotate a cube 30 degrees about the y-axis.
#
import pyvista
mesh = pyvista.Cube()
rot = mesh.rotate_y(30, inplace=False)
#
# Plot the rotated mesh.
#
pl = pyvista.Plotter()
_ = pl.add_mesh(rot)
_ = pl.add_mesh(mesh, style='wireframe', line_width=3)
_ = pl.add_axes_at_origin()
pl.show()
