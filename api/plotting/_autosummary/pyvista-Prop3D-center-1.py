import pyvista as pv
pl = pv.Plotter()
actor = pl.add_mesh(pv.Sphere(center=(0.5, 0.5, 1)))
actor.center  # doctest:+SKIP
# Expected:
## (0.5, 0.5, 1)
