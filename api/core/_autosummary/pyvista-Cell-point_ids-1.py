import pyvista
mesh = pyvista.Sphere()
mesh.get_cell(0).point_ids
# Expected:
## [2, 30, 0]
