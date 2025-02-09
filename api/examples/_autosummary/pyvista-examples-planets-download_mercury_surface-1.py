from pyvista import examples
texture = examples.planets.download_mercury_surface(texture=True)
texture.plot(zoom='tight', show_axes=False)
#
# .. seealso::
#
#     :ref:`Mercury Surface Dataset <mercury_surface_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :func:`~pyvista.examples.planets.load_mercury`
#         Load Mercury as a textured sphere.
#
#     :ref:`planets_example`
