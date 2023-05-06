import pyvista
from pyvista import examples
filename = examples.download_meshio_xdmf(load=False)
reader = pyvista.get_reader(filename)
filename.split("/")[-1]  # omit the path
# Expected:
## 'out.xdmf'
mesh = reader.read()
mesh.plot()
