import pyvista
grid = pyvista.ImageData(dimensions=(2, 2, 2))
grid.x
# Expected:
## array([0., 1., 0., 1., 0., 1., 0., 1.])
