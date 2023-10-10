import pyvista as pv
import numpy as np
xrng = np.arange(-10, 10, 1, dtype=np.float32)
yrng = np.arange(-10, 10, 2, dtype=np.float32)
zrng = np.arange(-10, 10, 5, dtype=np.float32)
x, y, z = np.meshgrid(xrng, yrng, zrng, indexing='ij')
grid = pv.StructuredGrid(x, y, z)
grid.dimensions
# Expected:
## (20, 10, 4)
