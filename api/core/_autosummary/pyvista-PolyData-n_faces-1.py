import pyvista as pv
plane = pv.Plane(i_resolution=2, j_resolution=2)
plane.n_faces
# Expected:
## 4
