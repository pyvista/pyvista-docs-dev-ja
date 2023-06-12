import pyvista
grid = pyvista.ImageData(dimensions=(2, 2, 2))
grid.y
# Expected:
## array([0., 0., 1., 1., 0., 0., 1., 1.])
