import pyvista as pv
from pyvista import examples
mesh = examples.planets.load_earth()
texture = examples.load_globe_texture()
image_path = examples.planets.download_stars_sky_background(load=False)
mesh.plot(texture=texture, background=image_path)
#
# .. seealso::
#
#     :func:`~pyvista.examples.examples.load_globe_texture`
#         Download the surface of the Earth.
#
#     :ref:`planets_example`
