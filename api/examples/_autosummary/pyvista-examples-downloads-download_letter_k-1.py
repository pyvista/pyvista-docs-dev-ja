from pyvista import examples
dataset = examples.download_letter_k()
dataset.plot(cpos="xy")
