from pyvista import examples
texture = examples.planets.download_saturn_rings(texture=True)
texture.plot(cpos='xy')
