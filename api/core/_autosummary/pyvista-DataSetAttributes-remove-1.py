# Add a point data array to a DataSet and then remove it.
#
import pyvista
mesh = pyvista.Cube()
mesh.point_data['my_data'] = range(mesh.n_points)
mesh.point_data.remove('my_data')
#
# Show that the array no longer exists in ``point_data``.
#
'my_data' in mesh.point_data
# Expected:
## False
