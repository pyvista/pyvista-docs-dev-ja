from pyvista import examples
dataset = examples.download_gourds_texture()
dataset.plot(cpos="xy")
