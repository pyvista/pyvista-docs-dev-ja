# Shows an interactive plane used specifically for slicing.
#
import pyvista as pv
from pyvista import examples
pl = pv.Plotter()
mesh = examples.load_channels()
_ = pl.add_mesh(mesh.outline())
_ = pl.add_mesh_slice(mesh, normal=[1, 0, 0.3])
pl.show()
