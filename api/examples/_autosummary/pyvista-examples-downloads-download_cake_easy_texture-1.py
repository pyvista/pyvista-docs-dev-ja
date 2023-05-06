from pyvista import examples
dataset = examples.download_cake_easy_texture()
dataset.plot(cpos="xy")
