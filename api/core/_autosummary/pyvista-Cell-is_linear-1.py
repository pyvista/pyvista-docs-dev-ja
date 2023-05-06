import pyvista
mesh = pyvista.Sphere()
mesh.get_cell(0).is_linear
# Expected:
## True
