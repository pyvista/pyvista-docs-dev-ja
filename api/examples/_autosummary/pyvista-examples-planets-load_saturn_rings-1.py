import pyvista as pv
from pyvista import examples
mesh = examples.planets.load_saturn_rings()
texture = examples.planets.download_saturn_rings(texture=True)
image_path = examples.planets.download_stars_sky_background(load=False)
mesh.plot(texture=texture, background=image_path)
#
# .. seealso::
#
#     :func:`~pyvista.examples.planets.download_saturn_rings`
#         Download the texture of Saturn's rings.
#
#     :func:`~pyvista.examples.planets.load_saturn`
#         Load the planet Saturn as a textured sphere.
#
#     :func:`~pyvista.examples.planets.download_saturn_surface`
#         Download the surface of Saturn.
#
#     :ref:`planets_example`
