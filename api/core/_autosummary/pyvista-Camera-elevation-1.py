import pyvista as pv
pl = pv.Plotter()
pl.camera.elevation
# Expected:
## 0.0
pl.camera.elevation = 45.0
pl.camera.elevation
# Expected:
## 45.0
