import pyvista as pv
pl = pv.Plotter()
_ = pl.add_mesh(pv.Sphere())
_ = pl.add_bounding_box(line_width=5, color='black')
pl.show()
