import pyvista as pv
from pyvista import examples
mesh = examples.planets.load_jupiter()
texture = examples.planets.download_jupiter_surface(texture=True)
image_path = examples.planets.download_stars_sky_background(load=False)
mesh.plot(texture=texture, background=image_path)
#
# .. seealso::
#
#     :func:`~pyvista.examples.planets.download_jupiter_surface`
#         Download the surface of Jupiter.
#
#     :ref:`planets_example`
