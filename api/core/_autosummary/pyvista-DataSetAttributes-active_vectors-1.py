# Associate point data to a simple cube mesh and show that the
# active vectors in the point array are the most recently added
# array.
#
import pyvista as pv
import numpy as np
mesh = pv.Cube()
vectors = np.random.default_rng().random((mesh.n_points, 3))
mesh.point_data.set_vectors(vectors, 'my-vectors')
vectors_out = mesh.point_data.active_vectors
vectors_out.shape
# Expected:
## (8, 3)
