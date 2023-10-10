import pyvista as pv
mesh = pv.Sphere()
pl = pv.Plotter()
_ = pl.add_mesh(mesh, label='sphere')
_ = pl.add_legend()
pl.remove_legend()
