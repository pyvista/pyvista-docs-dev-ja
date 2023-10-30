import numpy as np
import pyvista as pv
grid = pv.ImageData(dimensions=(3, 3, 3))
x, y, z = grid.points.T
r, phi, theta = pv.cartesian_to_spherical(x, y, z)
