import pyvista as pv
grid = pv.ImageData(dimensions=(2, 2, 2))
grid.z
# Expected:
## array([0., 0., 0., 0., 1., 1., 1., 1.])
