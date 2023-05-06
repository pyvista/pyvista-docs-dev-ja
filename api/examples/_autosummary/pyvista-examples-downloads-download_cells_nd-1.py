from pyvista import examples
dataset = examples.download_cells_nd()
dataset.plot(cpos="xy")
