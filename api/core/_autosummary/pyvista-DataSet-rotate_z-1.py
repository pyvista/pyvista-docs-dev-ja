# Rotate a mesh 30 degrees about the z-axis.
#
import pyvista
mesh = pyvista.Cube()
rot = mesh.rotate_z(30, inplace=False)
#
# Plot the rotated mesh.
#
pl = pyvista.Plotter()
_ = pl.add_mesh(rot)
_ = pl.add_mesh(mesh, style='wireframe', line_width=3)
_ = pl.add_axes_at_origin()
pl.show()
