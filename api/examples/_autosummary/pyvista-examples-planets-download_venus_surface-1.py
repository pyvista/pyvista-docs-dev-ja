from pyvista import examples
texture = examples.planets.download_venus_surface(texture=True)
texture.plot(zoom='tight', show_axes=False)
#
# .. seealso::
#
#     :ref:`Venus Surface Dataset <venus_surface_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :func:`~pyvista.examples.planets.load_venus`
#         Load Venus as a textured sphere.
#
#     :ref:`planets_example`
