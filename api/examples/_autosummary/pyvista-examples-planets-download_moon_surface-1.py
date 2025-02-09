from pyvista import examples
texture = examples.planets.download_moon_surface(texture=True)
texture.plot(zoom='tight', show_axes=False)
#
# .. seealso::
#
#     :ref:`Moon Surface Dataset <moon_surface_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :func:`~pyvista.examples.planets.load_moon`
#         Load the Moon as a textured sphere.
#
#     :ref:`planets_example`
