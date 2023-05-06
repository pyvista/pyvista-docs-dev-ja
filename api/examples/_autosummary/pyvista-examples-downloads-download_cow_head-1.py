from pyvista import examples
dataset = examples.download_cow_head()
dataset.plot(cpos="xy")
