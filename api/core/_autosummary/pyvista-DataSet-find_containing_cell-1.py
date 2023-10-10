# A unit square with 16 equal sized cells is created and a cell
# containing the point ``[0.3, 0.3, 0.0]`` is found.
#
import pyvista as pv
mesh = pv.ImageData(
    dimensions=[5, 5, 1], spacing=[1 / 4, 1 / 4, 0]
)
mesh
# Expected:
## ImageData...
mesh.find_containing_cell([0.3, 0.3, 0.0])
# Expected:
## 5
#
# A point outside the mesh domain will return ``-1``.
#
mesh.find_containing_cell([0.3, 0.3, 1.0])
# Expected:
## -1
#
# Find the cells that contain 1000 random points inside the mesh.
#
import numpy as np
points = np.random.random((1000, 3))
indices = mesh.find_containing_cell(points)
indices.shape
# Expected:
## (1000,)
