# First, compute cell normals.
#
import pyvista as pv
mesh = pv.Plane(i_resolution=1, j_resolution=1)
mesh_w_normals = mesh.compute_normals()
mesh_w_normals.point_data.active_normals_name
# Expected:
## 'Normals'
