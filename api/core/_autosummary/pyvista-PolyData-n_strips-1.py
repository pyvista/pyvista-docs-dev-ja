# Create a simple mesh with one triangle strip and return the
# number of triangles.
#
import pyvista as pv
import numpy as np
vertices = np.array(
    [[1.0, 0.0, 0.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]
)
strip = np.array([3, 0, 1, 2])
mesh = pv.PolyData(vertices, strips=strip)
mesh.n_strips
# Expected:
## 1
