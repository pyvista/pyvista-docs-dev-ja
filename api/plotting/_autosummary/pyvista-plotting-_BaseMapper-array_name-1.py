# Show the name of the active scalars in the mapper.
#
import pyvista as pv
mesh = pv.Sphere()
mesh['my_scalars'] = mesh.points[:, 2]
pl = pv.Plotter()
actor = pl.add_mesh(mesh, scalars='my_scalars')
actor.mapper.array_name
# Expected:
## 'my_scalars'
pl.close()
