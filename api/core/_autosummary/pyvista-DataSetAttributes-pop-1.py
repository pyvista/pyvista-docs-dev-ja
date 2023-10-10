# Add a point data array to a DataSet and then remove it.
#
import pyvista as pv
mesh = pv.Cube()
mesh.point_data['my_data'] = range(mesh.n_points)
mesh.point_data.pop('my_data')
# Expected:
## pyvista_ndarray([0, 1, 2, 3, 4, 5, 6, 7])
#
# Show that the array no longer exists in ``point_data``.
#
'my_data' in mesh.point_data
# Expected:
## False
