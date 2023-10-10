# Show that the default return value for a non-existent key is
# ``None``.
#
import pyvista as pv
mesh = pv.Cube()
mesh.point_data['my_data'] = range(mesh.n_points)
mesh.point_data.get('my-other-data')
