import pyvista as pv
plotter = pv.Plotter()
frustum = plotter.camera.view_frustum(1.0)
frustum.n_points
# Expected:
## 8
frustum.n_cells
# Expected:
## 6
