import pyvista
plotter = pyvista.Plotter()
actor = plotter.add_mesh(pyvista.Sphere())
plotter.show()
zval = plotter.get_image_depth()
