import pyvista as pv
grid = pv.ImageData(dimensions=(2, 2, 2))
grid.x
# Expected:
## array([0., 1., 0., 1., 0., 1., 0., 1.])
