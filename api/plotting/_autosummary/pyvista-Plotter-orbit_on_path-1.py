# Plot an orbit around the earth.  Save the gif as a temporary file.
#
import os
from tempfile import mkdtemp
import pyvista as pv
from pyvista import examples
mesh = examples.load_globe()
texture = examples.load_globe_texture()
filename = os.path.join(mkdtemp(), 'orbit.gif')
plotter = pv.Plotter(window_size=[300, 300])
_ = plotter.add_mesh(
    mesh, texture=texture, smooth_shading=True
)
plotter.open_gif(filename)
viewup = [0, 0, 1]
orbit = plotter.generate_orbital_path(
    factor=2.0, n_points=24, shift=0.0, viewup=viewup
)
plotter.orbit_on_path(
    orbit, write_frames=True, viewup=viewup, step=0.02
)
