from pyvista import examples
dataset = examples.download_gourds_pnm()
dataset.plot(rgba=True, cpos="xy")
