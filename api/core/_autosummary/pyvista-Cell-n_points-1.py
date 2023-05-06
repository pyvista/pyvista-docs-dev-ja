import pyvista
mesh = pyvista.Sphere()
mesh.get_cell(0).n_points
# Expected:
## 3
