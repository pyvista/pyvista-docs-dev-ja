import pyvista
from pyvista import examples
filename = examples.download_vtk_logo(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'vtk.png'
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh.plot()
