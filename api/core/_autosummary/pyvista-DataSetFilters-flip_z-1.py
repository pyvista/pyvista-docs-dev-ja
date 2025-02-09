import pyvista as pv
from pyvista import examples
pl = pv.Plotter(shape=(1, 2))
pl.subplot(0, 0)
pl.show_axes()
mesh1 = examples.download_teapot().rotate_x(90, inplace=False)
_ = pl.add_mesh(mesh1)
pl.subplot(0, 1)
pl.show_axes()
mesh2 = mesh1.flip_z(inplace=False)
_ = pl.add_mesh(mesh2)
pl.show(cpos='xz')
