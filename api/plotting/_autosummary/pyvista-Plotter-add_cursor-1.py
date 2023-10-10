import pyvista as pv
sphere = pv.Sphere()
plotter = pv.Plotter()
_ = plotter.add_mesh(sphere)
_ = plotter.add_cursor()
plotter.show()
