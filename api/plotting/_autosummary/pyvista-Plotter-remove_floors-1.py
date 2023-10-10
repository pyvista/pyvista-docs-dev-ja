# Add a floor below a sphere, remove it, and then plot it.
#
import pyvista as pv
pl = pv.Plotter()
actor = pl.add_mesh(pv.Sphere())
actor = pl.add_floor()
pl.remove_floors()
pl.show()
