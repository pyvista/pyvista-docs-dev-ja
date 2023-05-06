from pyvista import examples
dataset = examples.download_dolfin()
dataset.plot(cpos="xy", show_edges=True)
