from pyvista import examples
dataset = examples.download_bird_texture()
dataset.plot(cpos="xy")
