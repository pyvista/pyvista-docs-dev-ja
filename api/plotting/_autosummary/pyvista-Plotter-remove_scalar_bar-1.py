# Remove a scalar bar from a plotter.
#
import pyvista as pv
mesh = pv.Sphere()
mesh['data'] = mesh.points[:, 2]
pl = pv.Plotter()
_ = pl.add_mesh(mesh, cmap='coolwarm')
pl.remove_scalar_bar()
pl.show()
