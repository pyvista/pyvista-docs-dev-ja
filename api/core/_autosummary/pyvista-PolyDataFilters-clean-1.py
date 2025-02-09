# Create a mesh with a degenerate face and then clean it,
# removing the degenerate face
#
import pyvista as pv
import numpy as np
points = np.array([[0, 0, 0], [0, 1, 0], [1, 0, 0]], dtype=np.float32)
faces = np.array([3, 0, 1, 2, 3, 0, 2, 2])
mesh = pv.PolyData(points, faces)
mout = mesh.clean()
mout.faces  # doctest:+SKIP
# Expected:
## array([3, 0, 1, 2])
