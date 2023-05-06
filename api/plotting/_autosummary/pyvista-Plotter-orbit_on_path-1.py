# Plot an orbit around the earth.  Save the gif as a temporary file.
#
import os
from tempfile import mkdtemp
import pyvista
from pyvista import examples
filename = os.path.join(mkdtemp(), 'orbit.gif')
plotter = pyvista.Plotter(window_size=[300, 300])
_ = plotter.add_mesh(
    examples.load_globe(), smooth_shading=True
)
plotter.open_gif(filename)
viewup = [0, 0, 1]
orbit = plotter.generate_orbital_path(
    factor=2.0, n_points=24, shift=0.0, viewup=viewup
)
plotter.orbit_on_path(
    orbit, write_frames=True, viewup=viewup, step=0.02
)
