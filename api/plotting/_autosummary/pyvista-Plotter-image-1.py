import pyvista as pv
pl = pv.Plotter(off_screen=True)
_ = pl.add_mesh(pv.Cube())
pl.show()
pl.image  # doctest:+SKIP
