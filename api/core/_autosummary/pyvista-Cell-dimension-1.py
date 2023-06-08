import pyvista as pv
mesh = pv.Sphere()
mesh.get_cell(0).dimension
# Expected:
## 2
