# Shows an interactive slider controlling the altitude of the contours.
#
import pyvista as pv
from pyvista import examples
pl = pv.Plotter()
mesh = examples.load_random_hills()
_ = pl.add_mesh(mesh, opacity=0.4)
_ = pl.add_mesh_isovalue(mesh)
pl.show()
