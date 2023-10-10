import pyvista as pv
plotter = pv.Plotter()
actor = plotter.add_mesh(pv.Sphere())
plotter.show()
zval = plotter.get_image_depth()
