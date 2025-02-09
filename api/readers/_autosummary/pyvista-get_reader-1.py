import pyvista as pv
from pyvista import examples
filename = examples.download_human(load=False)
filename.split('/')[-1]  # omit the path
# Expected:
## 'Human.vtp'
reader = pv.get_reader(filename)
reader
# Expected:
## XMLPolyDataReader('.../Human.vtp')
mesh = reader.read()
mesh
# Expected:
## PolyData ...
mesh.plot(color='lightblue')
