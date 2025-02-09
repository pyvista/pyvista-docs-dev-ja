from pyvista import examples
texture = examples.planets.download_jupiter_surface(texture=True)
texture.plot(zoom='tight', show_axes=False)
#
# .. seealso::
#
#     :ref:`Jupiter Surface Dataset <jupiter_surface_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :func:`~pyvista.examples.planets.load_jupiter`
#         Load Jupiter as a textured sphere.
#
#     :ref:`planets_example`
