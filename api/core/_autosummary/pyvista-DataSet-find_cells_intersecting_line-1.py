import pyvista
mesh = pyvista.Sphere()
mesh.find_cells_intersecting_line([0.0, 0, 0], [1.0, 0, 0])
# Expected:
## array([  86, 1653])
