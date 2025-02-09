import pyvista as pv
from pyvista import examples
filename = examples.download_lobster(load=False)
filename.split('/')[-1]  # omit the path
# Expected:
## 'lobster.ply'
reader = pv.get_reader(filename)
mesh = reader.read()
mesh.plot()
