# Add random vectors to a mesh as point data.
#
import pyvista
import numpy as np
mesh = pyvista.Cube()
mesh.clear_data()
vectors = np.random.random((mesh.n_points, 3))
mesh.point_data.set_vectors(vectors, 'my-vectors')
mesh.point_data
# Expected:
## pyvista DataSetAttributes
## Association     : POINT
## Active Scalars  : None
## Active Vectors  : my-vectors
## Active Texture  : None
## Active Normals  : None
## Contains arrays :
##     my-vectors              float64    (8, 3)               VECTORS
