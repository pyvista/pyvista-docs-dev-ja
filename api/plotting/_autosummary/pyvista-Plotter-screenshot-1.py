import pyvista as pv
sphere = pv.Sphere()
plotter = pv.Plotter(off_screen=True)
actor = plotter.add_mesh(sphere)
plotter.screenshot('screenshot.png')  # doctest:+SKIP
