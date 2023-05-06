import pyvista as pv
mesh = pv.Cone()
pl = pv.Plotter()
_ = pl.add_mesh(mesh)
_ = pl.show_grid()
pl.show()
