from pyvista import examples
dataset = examples.download_vtk_logo()
dataset.plot(cpos="xy")
