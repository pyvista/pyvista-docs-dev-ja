# Store data with point association in a DataSet.
#
import pyvista as pv
mesh = pv.Cube()
mesh.point_data['my_data'] = range(mesh.n_points)
data = mesh.point_data['my_data']
data
# Expected:
## pyvista_ndarray([0, 1, 2, 3, 4, 5, 6, 7])
#
# Change the data array and show that this is reflected in the DataSet.
#
data[:] = 0
mesh.point_data['my_data']
# Expected:
## pyvista_ndarray([0, 0, 0, 0, 0, 0, 0, 0])
#
# Remove the array.
#
del mesh.point_data['my_data']
'my_data' in mesh.point_data
# Expected:
## False
#
# Print the available arrays from dataset attributes.
#
import numpy as np
mesh = pv.Plane(i_resolution=1, j_resolution=1)
mesh.point_data.set_array(range(4), 'my-data')
mesh.point_data.set_array(range(5, 9), 'my-other-data')
vectors0 = np.random.random((4, 3))
mesh.point_data.set_vectors(vectors0, 'vectors0')
vectors1 = np.random.random((4, 3))
mesh.point_data.set_vectors(vectors1, 'vectors1')
mesh.point_data
# Expected:
## pyvista DataSetAttributes
## Association     : POINT
## Active Scalars  : None
## Active Vectors  : vectors1
## Active Texture  : TextureCoordinates
## Active Normals  : Normals
## Contains arrays :
##     Normals                 float32    (4, 3)               NORMALS
##     TextureCoordinates      float32    (4, 2)               TCOORDS
##     my-data                 int64      (4,)
##     my-other-data           int64      (4,)
##     vectors1                float64    (4, 3)               VECTORS
##     vectors0                float64    (4, 3)
