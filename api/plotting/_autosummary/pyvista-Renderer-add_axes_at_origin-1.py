import pyvista as pv
pl = pv.Plotter()
_ = pl.add_mesh(pv.Sphere(center=(2, 0, 0)), color='r')
_ = pl.add_mesh(pv.Sphere(center=(0, 2, 0)), color='g')
_ = pl.add_mesh(pv.Sphere(center=(0, 0, 2)), color='b')
_ = pl.add_axes_at_origin()
pl.show()
