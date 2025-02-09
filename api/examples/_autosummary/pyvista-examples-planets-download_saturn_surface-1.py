from pyvista import examples
texture = examples.planets.download_saturn_surface(texture=True)
texture.plot(zoom='tight', show_axes=False)
#
# .. seealso::
#
#     :ref:`Saturn Surface Dataset <saturn_surface_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :func:`~pyvista.examples.planets.load_saturn`
#         Load the planet Saturn as a textured sphere.
#
#     :func:`~pyvista.examples.planets.load_saturn_rings`
#         Load Saturn's rings as a textured disc.
#
#     :func:`~pyvista.examples.planets.download_saturn_rings`
#         Download the texture of Saturn's rings.
#
#     :ref:`planets_example`
