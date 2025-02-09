import pyvista as pv
from pyvista import examples
mesh = examples.planets.load_pluto()
texture = examples.planets.download_pluto_surface(texture=True)
image_path = examples.planets.download_stars_sky_background(load=False)
mesh.plot(texture=texture, background=image_path)
#
# .. seealso::
#
#     :func:`~pyvista.examples.planets.download_pluto_surface`
#         Download the surface of Pluto.
#
#     :ref:`planets_example`
