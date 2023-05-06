from pyvista import examples
mesh = examples.download_bunny()
mesh.plot(cpos=bunny_cpos, anti_aliasing='ssao')