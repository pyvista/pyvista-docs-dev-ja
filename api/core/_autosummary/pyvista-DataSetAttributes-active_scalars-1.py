# Associate point data to a simple cube mesh and show that the
# active scalars in the point array are the most recently added
# array.
#
import pyvista as pv
import numpy as np
mesh = pv.Cube()
mesh.point_data['data0'] = np.arange(mesh.n_points)
mesh.point_data.active_scalars
# Expected:
## pyvista_ndarray([0, 1, 2, 3, 4, 5, 6, 7])
