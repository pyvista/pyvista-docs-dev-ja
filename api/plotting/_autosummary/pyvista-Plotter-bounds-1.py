import pyvista as pv
pl = pv.Plotter()
_ = pl.add_mesh(pv.Cube())
pl.bounds
# Expected:
## BoundsTuple(x_min=-0.5, x_max=0.5, y_min=-0.5, y_max=0.5, z_min=-0.5, z_max=0.5)
