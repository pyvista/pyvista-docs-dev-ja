from pyvista import examples
texture = examples.planets.download_neptune_surface(texture=True)
texture.plot(zoom='tight', show_axes=False)
#
# .. seealso::
#
#     :ref:`Neptune Surface Dataset <neptune_surface_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :func:`~pyvista.examples.planets.load_neptune`
#         Load Neptune as a textured sphere.
#
#     :ref:`planets_example`
