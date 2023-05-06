from pyvista import examples
dataset = examples.download_vtk()
dataset.plot(cpos="xy", line_width=5)
