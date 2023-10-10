import pyvista as pv
pl = pv.Plotter()
pl.camera.clipping_range
# Expected:
## (0.01, 1000.01)
pl.camera.clipping_range = (1, 10)
pl.camera.clipping_range
# Expected:
## (1.0, 10.0)
