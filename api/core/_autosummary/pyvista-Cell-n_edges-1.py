import pyvista
mesh = pyvista.Sphere()
mesh.get_cell(0).n_edges
# Expected:
## 3
