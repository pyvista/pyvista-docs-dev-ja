from pyvista import examples
dataset = examples.download_bird()
dataset.plot(rgba=True, cpos="xy")
