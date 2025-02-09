from pyvista import examples
texture = examples.planets.download_mars_surface(texture=True)
texture.plot(zoom='tight', show_axes=False)
#
# .. seealso::
#
#     :ref:`Mars Surface Dataset <mars_surface_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :func:`~pyvista.examples.planets.load_mars`
#         Load Mars as a textured sphere.
#
#     :ref:`planets_example`
