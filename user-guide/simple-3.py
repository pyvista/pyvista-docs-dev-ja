mesh = examples.load_airplane()

plotter = pv.Plotter()    # instantiate the plotter
plotter.add_mesh(mesh)    # add a mesh to the scene
plotter.camera.zoom(2)    # Note how we can now access underlying attributes
plotter.show()            # show the rendering window