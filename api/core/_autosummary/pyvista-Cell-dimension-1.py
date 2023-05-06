import pyvista
mesh = pyvista.Sphere()
mesh.get_cell(0).dimension
# Expected:
## 2
