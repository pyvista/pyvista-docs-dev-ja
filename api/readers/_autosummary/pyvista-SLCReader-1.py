import pyvista
from pyvista import examples
filename = examples.download_knee_full(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'vw_knee.slc'
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh.plot()
