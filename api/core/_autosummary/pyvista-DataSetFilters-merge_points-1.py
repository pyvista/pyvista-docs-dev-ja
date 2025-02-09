# Merge duplicate points in a mesh.
#
import pyvista as pv
mesh = pv.Cylinder(resolution=4)
mesh.n_points
# Expected:
## 16
_ = mesh.merge_points(inplace=True)
mesh.n_points
# Expected:
## 8
