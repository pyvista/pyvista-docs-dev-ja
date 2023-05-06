from pyvista import examples
dataset = examples.download_emoji_texture()
dataset.plot(cpos="xy")
