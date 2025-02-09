import pyvista as pv
pl = pv.Plotter()
mesh = pv.Cube(x_length=0.1, y_length=0.2, z_length=0.3)
actor = pl.add_mesh(mesh)
actor.bounds
# Expected:
## BoundsTuple(x_min=-0.05, x_max=0.05, y_min=-0.1, y_max=0.1, z_min=-0.15, z_max=0.15)
