from pyvista import examples
dataset = examples.download_usa()
dataset.plot(style="wireframe", cpos="xy")
