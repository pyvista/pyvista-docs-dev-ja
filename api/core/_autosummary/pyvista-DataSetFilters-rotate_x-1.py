# Rotate a mesh 30 degrees about the x-axis.
#
import pyvista as pv
mesh = pv.Cube()
rot = mesh.rotate_x(30, inplace=False)
#
# Plot the rotated mesh.
#
pl = pv.Plotter()
_ = pl.add_mesh(rot)
_ = pl.add_mesh(mesh, style='wireframe', line_width=3)
_ = pl.add_axes_at_origin()
pl.show()
