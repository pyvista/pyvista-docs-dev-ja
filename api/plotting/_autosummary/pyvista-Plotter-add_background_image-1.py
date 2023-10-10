import pyvista as pv
from pyvista import examples
plotter = pv.Plotter()
actor = plotter.add_mesh(pv.Sphere())
plotter.add_background_image(examples.mapfile)
plotter.show()
