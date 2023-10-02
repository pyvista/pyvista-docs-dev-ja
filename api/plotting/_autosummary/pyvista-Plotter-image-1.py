import pyvista
pl = pyvista.Plotter(off_screen=True)
_ = pl.add_mesh(pyvista.Cube())
pl.show()
pl.image  # doctest:+SKIP
