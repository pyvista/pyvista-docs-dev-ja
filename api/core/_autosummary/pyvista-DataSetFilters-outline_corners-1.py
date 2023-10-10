# Generate and plot the corners of a sphere.  This is
# effectively the ``(x, y, z)`` bounds of the mesh.
#
import pyvista as pv
sphere = pv.Sphere()
corners = sphere.outline_corners(factor=0.1)
pv.plot([sphere, corners], line_width=5)
