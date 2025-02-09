from pyvista import examples
texture = examples.planets.download_pluto_surface(texture=True)
texture.plot(zoom='tight', show_axes=False)
#
# .. seealso::
#
#     :ref:`Pluto Surface Dataset <pluto_surface_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :func:`~pyvista.examples.planets.load_pluto`
#         Load Pluto as a textured sphere.
#
#     :ref:`planets_example`
