from pyvista import examples
dataset = examples.download_structured_grid_two()
dataset.plot(show_edges=True)
