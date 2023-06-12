from pyvista import examples
dataset = examples.load_globe()
texture = examples.load_globe_texture()
dataset.plot(texture=texture)
