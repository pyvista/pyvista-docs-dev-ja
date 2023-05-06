from pyvista import examples
dataset = examples.download_rgba_texture()
dataset.plot(cpos="xy")
