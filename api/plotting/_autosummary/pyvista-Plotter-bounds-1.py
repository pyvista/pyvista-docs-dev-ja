import pyvista
pl = pyvista.Plotter()
_ = pl.add_mesh(pyvista.Cube())
pl.bounds
# Expected:
## (-0.5, 0.5, -0.5, 0.5, -0.5, 0.5)
