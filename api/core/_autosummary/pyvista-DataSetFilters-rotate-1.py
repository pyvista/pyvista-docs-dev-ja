# Define a rotation. Here, a 3x3 matrix is used which rotates about the z-axis by
# 60 degrees.
#
import pyvista as pv
rotation = [
    [0.5, -0.8660254, 0.0],
    [0.8660254, 0.5, 0.0],
    [0.0, 0.0, 1.0],
]
#
# Use the rotation to rotate a cone about its tip.
#
mesh = pv.Cone()
tip = (0.5, 0.0, 0.0)
rot = mesh.rotate(rotation, point=tip)
#
# Plot the rotated mesh.
#
pl = pv.Plotter()
_ = pl.add_mesh(rot)
_ = pl.add_mesh(mesh, style='wireframe', line_width=3)
_ = pl.add_axes_at_origin()
pl.show()
