from pyvista import examples
dataset = examples.download_structured_grid()
dataset.plot(show_edges=True)
