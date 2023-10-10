# Create two meshes and overwrite ``mesh_a`` with ``mesh_b``.
# Show that ``mesh_a`` is equal to ``mesh_b``.
#
import pyvista as pv
mesh_a = pv.Sphere()
mesh_b = pv.Cube()
mesh_a.copy_from(mesh_b)
mesh_a == mesh_b
# Expected:
## True
