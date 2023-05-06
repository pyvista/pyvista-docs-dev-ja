from pyvista import examples
texture = examples.download_puppy_texture()
flipped = texture.flip_x()
flipped.plot()
