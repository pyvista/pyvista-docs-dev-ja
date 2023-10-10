# Shows an interactive plane sliced along each cartesian axis of the mesh.
#
import pyvista as pv
pl = pv.Plotter()
mesh = pv.Wavelet()
_ = pl.add_mesh(mesh.outline())
_ = pl.add_mesh_slice_orthogonal(mesh)
pl.show()
