import pyvista as pv
plotter = pv.Plotter()
actor = plotter.add_mesh(pv.Sphere())
plotter.clear()
plotter.renderer.actors
# Expected:
## {}
