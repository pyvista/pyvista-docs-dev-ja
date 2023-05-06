from pyvista import examples
dataset = examples.download_disc_quads()
dataset.plot(show_edges=True)
