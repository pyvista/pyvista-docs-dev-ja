# Move the camera far away to ``[7, 7, 7]``.
#
import pyvista as pv
mesh = pv.Cube()
pl = pv.Plotter()
_ = pl.add_mesh(mesh, show_edges=True)
pl.set_position([7, 7, 7])
pl.show()
