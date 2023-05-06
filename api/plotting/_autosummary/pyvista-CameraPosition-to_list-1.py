import pyvista
pl = pyvista.Plotter()
pl.camera_position.to_list()
# Expected:
## [(0.0, 0.0, 1.0), (0.0, 0.0, 0.0), (0.0, 1.0, 0.0)]
