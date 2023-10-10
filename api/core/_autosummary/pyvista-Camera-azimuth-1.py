import pyvista as pv
pl = pv.Plotter()
pl.camera.azimuth
# Expected:
## 0.0
pl.camera.azimuth = 45.0
pl.camera.azimuth
# Expected:
## 45.0
