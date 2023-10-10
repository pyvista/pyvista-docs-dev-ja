# Add a floor below a sphere and plot it.
#
import pyvista as pv
pl = pv.Plotter()
actor = pl.add_mesh(pv.Sphere())
actor = pl.add_floor()
pl.show()
