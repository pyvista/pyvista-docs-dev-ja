from pyvista import examples
texture = examples.download_puppy_texture()
rotated = texture.rotate_ccw()
rotated.plot()
