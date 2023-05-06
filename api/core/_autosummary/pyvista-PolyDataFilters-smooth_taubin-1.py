# Smooth the example bone mesh. Here, it's necessary to subdivide the
# mesh to increase the number of faces as the original mesh is so coarse.
#
import pyvista as pv
from pyvista import examples
mesh = examples.download_foot_bones().subdivide(2)
smoothed_mesh = mesh.smooth_taubin()
pl = pv.Plotter(shape=(1, 2))
_ = pl.add_mesh(mesh)
_ = pl.add_text('Original Mesh')
pl.subplot(0, 1)
_ = pl.add_mesh(smoothed_mesh)
_ = pl.add_text('Smoothed Mesh')
pl.show()
