# Shows an interactive clip box.
#
import pyvista as pv
mesh = pv.ParametricConicSpiral()
pl = pv.Plotter()
_ = pl.add_mesh_clip_box(mesh, color='white')
pl.show()
