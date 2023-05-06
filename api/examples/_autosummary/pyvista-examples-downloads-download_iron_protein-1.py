from pyvista import examples
dataset = examples.download_iron_protein()
dataset.plot(volume=True, cmap='blues')
