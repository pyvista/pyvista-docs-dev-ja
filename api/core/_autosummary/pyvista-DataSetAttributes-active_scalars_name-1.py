# Add two arrays to the mesh point data. Note how the first array becomes
# the active scalars since the ``mesh`` contained no scalars.
#
import pyvista
mesh = pyvista.Sphere()
mesh.point_data['my_data'] = range(mesh.n_points)
mesh.point_data['my_other_data'] = range(mesh.n_points)
mesh.point_data.active_scalars_name
# Expected:
## 'my_data'
#
# Set the name of the active scalars.
#
mesh.point_data.active_scalars_name = 'my_other_data'
mesh.point_data.active_scalars_name
# Expected:
## 'my_other_data'
