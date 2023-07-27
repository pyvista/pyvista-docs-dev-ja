import pyvista
mesh = pyvista.Sphere()
mesh.find_cells_along_line([0.0, 0, 0], [1.0, 0, 0])
# Expected:
## array([  86,   87, 1652, 1653])
