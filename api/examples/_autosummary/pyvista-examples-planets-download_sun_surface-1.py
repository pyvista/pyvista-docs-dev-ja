from pyvista import examples
texture = examples.planets.download_sun_surface(texture=True)
texture.plot(zoom='tight', show_axes=False)
#
# .. seealso::
#
#     :ref:`Sun Surface Dataset <sun_surface_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :func:`~pyvista.examples.planets.load_sun`
#         Load the Sun as a textured sphere.
#
#     :ref:`planets_example`
