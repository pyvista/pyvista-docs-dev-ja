import pyvista as pv
cone = pv.Cone(height=2.0, radius=0.5)
pl = pv.Plotter()
_ = pl.add_mesh(cone)
_ = pl.add_legend_scale()
pl.show()
