import pyvista as pv
pl = pv.Plotter()
_ = pl.add_mesh(pv.Sphere())
pl.camera.clipping_range = (1, 2)
pl.camera.reset_clipping_range()  # doctest:+SKIP
# Expected:
## (0.0039213485598532955, 3.9213485598532953)
