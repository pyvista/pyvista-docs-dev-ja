from pyvista import examples
dataset = examples.download_unstructured_grid()
dataset.plot(show_edges=True)
