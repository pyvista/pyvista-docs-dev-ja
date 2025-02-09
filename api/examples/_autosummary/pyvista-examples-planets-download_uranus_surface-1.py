from pyvista import examples
texture = examples.planets.download_uranus_surface(texture=True)
texture.plot(zoom='tight', show_axes=False)
#
# .. seealso::
#
#     :ref:`Uranus Surface Dataset <uranus_surface_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :func:`~pyvista.examples.planets.load_uranus`
#         Load Uranus as a textured sphere.
#
#     :ref:`planets_example`
