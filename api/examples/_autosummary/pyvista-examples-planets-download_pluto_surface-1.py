from pyvista import examples
texture = examples.planets.download_pluto_surface(texture=True)
texture.plot(zoom='tight', show_axes=False)
