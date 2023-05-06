from pyvista import examples
texture = examples.planets.download_mercury_surface(texture=True)
texture.plot(zoom='tight', show_axes=False)
