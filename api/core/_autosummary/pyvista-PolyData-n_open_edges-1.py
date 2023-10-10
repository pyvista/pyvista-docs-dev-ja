# Return the number of open edges on a sphere.
#
import pyvista as pv
sphere = pv.Sphere()
sphere.n_open_edges
# Expected:
## 0
#
# Return the number of open edges on a plane.
#
plane = pv.Plane(i_resolution=1, j_resolution=1)
plane.n_open_edges
# Expected:
## 4
