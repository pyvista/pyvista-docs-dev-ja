import pyvista as pv
pl = pv.Plotter()
_ = pl.add_mesh(pv.Cube())
pl.bounds
# Expected:
## (-0.5, 0.5, -0.5, 0.5, -0.5, 0.5)
