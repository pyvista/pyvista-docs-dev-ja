import pyvista as pv
mesh = pv.Sphere()
mesh.get_cell(0).is_linear
# Expected:
## True
