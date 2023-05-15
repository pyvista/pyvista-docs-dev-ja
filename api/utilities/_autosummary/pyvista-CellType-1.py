# Create a single cube. Notice how the cell type is defined using the
# ``CellType``.
#
import numpy as np
from pyvista import CellType
import pyvista
cells = np.array([8, 0, 1, 2, 3, 4, 5, 6, 7])
cell_type = np.array([CellType.HEXAHEDRON], np.int8)
points = np.array(
    [
        [0, 0, 0],
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1],
    ],
    dtype=np.float32,
)
grid = pyvista.UnstructuredGrid(cells, cell_type, points)
grid
# Expected:
## UnstructuredGrid (...)
##   N Cells:    1
##   N Points:   8
##   X Bounds:   0.000e+00, 1.000e+00
##   Y Bounds:   0.000e+00, 1.000e+00
##   Z Bounds:   0.000e+00, 1.000e+00
##   N Arrays:   0
