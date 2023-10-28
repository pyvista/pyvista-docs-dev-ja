import pyvista as pv
pl = pv.Plotter()
mesh = pv.Cube(x_length=0.1, y_length=0.2, z_length=0.3)
actor = pl.add_mesh(mesh)
actor.bounds
# Expected:
## (-0.05, 0.05, -0.1, 0.1, -0.15, 0.15)
