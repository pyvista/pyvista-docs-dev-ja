from pyvista import examples
dataset = examples.download_puppy()
dataset.plot(cpos='xy', rgba=True)
