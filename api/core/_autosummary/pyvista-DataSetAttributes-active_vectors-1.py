# Associate point data to a simple cube mesh and show that the
# active vectors in the point array are the most recently added
# array.
#
import pyvista
import numpy as np
mesh = pyvista.Cube()
vectors = np.random.random((mesh.n_points, 3))
mesh.point_data.set_vectors(vectors, 'my-vectors')
vectors_out = mesh.point_data.active_vectors
vectors_out.shape
# Expected:
## (8, 3)
