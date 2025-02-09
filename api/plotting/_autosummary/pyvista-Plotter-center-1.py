import pyvista as pv
pl = pv.Plotter()
_ = pl.add_mesh(pv.Cube())
pl.center
# Expected:
## (0.0, 0.0, 0.0)
