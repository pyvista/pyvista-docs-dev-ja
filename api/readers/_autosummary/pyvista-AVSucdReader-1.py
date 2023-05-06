import pyvista
from pyvista import examples
filename = examples.download_cells_nd(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'cellsnd.ascii.inp'
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh.plot(cpos="xy")
