from pyvista import examples
dataset = examples.download_prostate()
dataset.plot(cpos="xy")
