# Add an array to ``point_data`` to a DataSet and then clear the
# point_data.
#
import pyvista
mesh = pyvista.Cube()
mesh.clear_data()
mesh.point_data['my_data'] = range(mesh.n_points)
len(mesh.point_data)
# Expected:
## 1
mesh.point_data.clear()
len(mesh.point_data)
# Expected:
## 0
