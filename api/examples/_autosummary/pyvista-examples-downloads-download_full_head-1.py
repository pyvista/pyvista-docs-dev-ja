from pyvista import examples
dataset = examples.download_full_head()
dataset.plot(volume=True)
