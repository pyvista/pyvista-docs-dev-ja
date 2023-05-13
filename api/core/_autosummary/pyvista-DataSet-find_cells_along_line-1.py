import pyvista
mesh = pyvista.Sphere()
mesh.find_cells_along_line([0.0, 0, 0], [1.0, 0, 0])
# Expected:
## array([842, 843, 896, 897])
