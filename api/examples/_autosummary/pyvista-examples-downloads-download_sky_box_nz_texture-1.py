from pyvista import examples
dataset = examples.download_sky_box_nz_texture()
dataset.plot(cpos="xy")
