import pyvista as pv
pl = pv.Plotter()
_ = pl.add_mesh(pv.Sphere())
pl.add_blurring()
pl.remove_blurring()
pl.show()
