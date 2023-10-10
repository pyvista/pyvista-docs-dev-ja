# Show a mesh from :func:`pyvista.Plane` is not composed of all
# triangles.
#
import pyvista as pv
plane = pv.Plane()
plane.is_all_triangles
# Expected:
## False
#
# Show that the mesh from :func:`pyvista.Sphere` contains only
# triangles.
#
sphere = pv.Sphere()
sphere.is_all_triangles
# Expected:
## True
