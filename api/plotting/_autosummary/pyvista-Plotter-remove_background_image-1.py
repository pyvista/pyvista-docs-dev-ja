import pyvista as pv
from pyvista import examples
pl = pv.Plotter(shape=(1, 2))
pl.subplot(0, 0)
actor = pl.add_mesh(pv.Sphere())
pl.add_background_image(examples.mapfile, as_global=False)
pl.subplot(0, 1)
actor = pl.add_mesh(pv.Cube())
pl.add_background_image(examples.mapfile, as_global=False)
pl.remove_background_image()
pl.show()
