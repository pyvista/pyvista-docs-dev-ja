from pyvista import examples
dataset = examples.download_delaunay_example()
dataset.plot(show_edges=True)
