import pyvista
pl = pyvista.Plotter()
_ = pl.add_mesh(pyvista.Cube())
pl.center
# Expected:
## [0.0, 0.0, 0.0]
