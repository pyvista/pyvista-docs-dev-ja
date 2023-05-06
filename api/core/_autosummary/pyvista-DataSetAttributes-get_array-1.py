# Store data with point association in a DataSet.
#
import pyvista
mesh = pyvista.Cube()
mesh.clear_data()
mesh.point_data['my_data'] = range(mesh.n_points)
#
# Access using an index.
#
mesh.point_data.get_array(0)
# Expected:
## pyvista_ndarray([0, 1, 2, 3, 4, 5, 6, 7])
#
# Access using a key.
#
mesh.point_data.get_array('my_data')
# Expected:
## pyvista_ndarray([0, 1, 2, 3, 4, 5, 6, 7])
