import pyvista as pv
from pyvista import examples
filename = examples.download_can_crushed_hdf(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'can-vtu.hdf'
reader = pv.get_reader(filename)
mesh = reader.read()
mesh.plot()
