import pyvista
from pyvista import examples
mesh = examples.load_globe()
texture = examples.load_globe_texture()
pl = pyvista.Plotter(shape=(1, 2))
pl.subplot(0, 0)
_ = pl.add_mesh(mesh, texture=texture)
pl.subplot(0, 1)
_ = pl.add_mesh(examples.load_airplane())
pl.show_axes_all()
pl.show()
