# Not linked view case.
#
import pyvista
from pyvista import demos
ocube = demos.orientation_cube()
pl = pyvista.Plotter(shape=(1, 2))
pl.subplot(0, 0)
_ = pl.add_mesh(ocube['cube'], show_edges=True)
_ = pl.add_mesh(ocube['x_p'], color='blue')
_ = pl.add_mesh(ocube['x_n'], color='blue')
_ = pl.add_mesh(ocube['y_p'], color='green')
_ = pl.add_mesh(ocube['y_n'], color='green')
_ = pl.add_mesh(ocube['z_p'], color='red')
_ = pl.add_mesh(ocube['z_n'], color='red')
pl.camera_position = 'yz'
pl.subplot(0, 1)
_ = pl.add_mesh(ocube['cube'], show_edges=True)
_ = pl.add_mesh(ocube['x_p'], color='blue')
_ = pl.add_mesh(ocube['x_n'], color='blue')
_ = pl.add_mesh(ocube['y_p'], color='green')
_ = pl.add_mesh(ocube['y_n'], color='green')
_ = pl.add_mesh(ocube['z_p'], color='red')
_ = pl.add_mesh(ocube['z_n'], color='red')
pl.show_axes()
pl.show()
#
# Linked view case.
#
pl = pyvista.Plotter(shape=(1, 2))
pl.subplot(0, 0)
_ = pl.add_mesh(ocube['cube'], show_edges=True)
_ = pl.add_mesh(ocube['x_p'], color='blue')
_ = pl.add_mesh(ocube['x_n'], color='blue')
_ = pl.add_mesh(ocube['y_p'], color='green')
_ = pl.add_mesh(ocube['y_n'], color='green')
_ = pl.add_mesh(ocube['z_p'], color='red')
_ = pl.add_mesh(ocube['z_n'], color='red')
pl.camera_position = 'yz'
pl.subplot(0, 1)
_ = pl.add_mesh(ocube['cube'], show_edges=True)
_ = pl.add_mesh(ocube['x_p'], color='blue')
_ = pl.add_mesh(ocube['x_n'], color='blue')
_ = pl.add_mesh(ocube['y_p'], color='green')
_ = pl.add_mesh(ocube['y_n'], color='green')
_ = pl.add_mesh(ocube['z_p'], color='red')
_ = pl.add_mesh(ocube['z_n'], color='red')
pl.show_axes()
pl.link_views()
pl.show()
