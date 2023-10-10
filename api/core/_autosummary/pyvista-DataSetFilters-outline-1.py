# Generate and plot the outline of a sphere.  This is
# effectively the ``(x, y, z)`` bounds of the mesh.
#
import pyvista as pv
sphere = pv.Sphere()
outline = sphere.outline()
pv.plot([sphere, outline], line_width=5)
