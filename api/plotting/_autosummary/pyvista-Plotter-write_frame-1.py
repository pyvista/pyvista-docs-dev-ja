import pyvista as pv
plotter = pv.Plotter()
plotter.open_movie(filename)  # doctest:+SKIP
plotter.add_mesh(pv.Sphere())  # doctest:+SKIP
plotter.write_frame()  # doctest:+SKIP
