import pyvista
from pyvista import examples
filename = examples.download_chest(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'ChestCT-SHORT.mha'
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh.plot()
