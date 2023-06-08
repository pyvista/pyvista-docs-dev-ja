import pyvista as pv
mesh = pv.Sphere()
mesh.get_cell(0).n_edges
# Expected:
## 3
