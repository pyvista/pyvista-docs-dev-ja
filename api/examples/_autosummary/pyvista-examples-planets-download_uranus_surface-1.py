from pyvista import examples
texture = examples.planets.download_uranus_surface(texture=True)
texture.plot(zoom='tight', show_axes=False)
