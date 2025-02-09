from pyvista import examples
texture = examples.planets.download_saturn_rings(texture=True)
texture.plot(cpos='xy')
#
# .. seealso::
#
#     :ref:`Saturn Rings Dataset <saturn_rings_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :func:`~pyvista.examples.planets.load_saturn_rings`
#         Load Saturn's rings as a textured disc.
#
#     :func:`~pyvista.examples.planets.load_saturn`
#         Load the planet Saturn as a textured sphere.
#
#     :func:`~pyvista.examples.planets.download_saturn_surface`
#         Download the surface of Saturn.
#
#     :ref:`planets_example`
