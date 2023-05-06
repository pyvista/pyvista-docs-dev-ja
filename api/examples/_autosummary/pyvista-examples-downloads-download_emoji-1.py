from pyvista import examples
dataset = examples.download_emoji()
dataset.plot(rgba=True, cpos="xy")
