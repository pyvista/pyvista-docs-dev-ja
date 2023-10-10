import pyvista as pv
import numpy as np
mesh = pv.Sphere()
mesh.point_data.set_vectors(
    np.random.random((mesh.n_points, 3)), 'my-vectors'
)
mesh.point_data.active_vectors_name
# Expected:
## 'my-vectors'
