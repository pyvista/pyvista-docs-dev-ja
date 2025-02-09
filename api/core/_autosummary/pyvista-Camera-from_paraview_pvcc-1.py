import pyvista as pv
pl = pv.Plotter()
pl.camera = pv.Camera.from_paraview_pvcc('camera.pvcc')  # doctest:+SKIP
pl.camera.position
# Expected:
## (1.0, 1.0, 1.0)
