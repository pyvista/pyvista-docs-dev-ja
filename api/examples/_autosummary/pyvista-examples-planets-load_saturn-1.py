import pyvista as pv
from pyvista import examples
mesh = examples.planets.load_saturn()
texture = examples.planets.download_saturn_surface(texture=True)
image_path = examples.planets.download_stars_sky_background(load=False)
mesh.plot(texture=texture, background=image_path)
#
# .. seealso::
#
#     :func:`~pyvista.examples.planets.download_saturn_surface`
#         Download the surface of Saturn.
#
#     :func:`~pyvista.examples.planets.load_saturn_rings`
#         Load Saturn's rings as a textured disc.
#
#     :func:`~pyvista.examples.planets.download_saturn_rings`
#         Download the texture of Saturn's rings.
#
#     :ref:`planets_example`
