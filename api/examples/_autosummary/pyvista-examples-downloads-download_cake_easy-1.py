from pyvista import examples
dataset = examples.download_cake_easy()
dataset.plot(rgba=True, cpos="xy")
