from pyvista import examples
dataset = examples.download_sky_box_nz()
dataset.plot(rgba=True, cpos="xy")
