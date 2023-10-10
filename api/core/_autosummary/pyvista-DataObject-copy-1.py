# Create and make a deep copy of a PolyData object.
#
import pyvista as pv
mesh_a = pv.Sphere()
mesh_b = mesh_a.copy()
mesh_a == mesh_b
# Expected:
## True
