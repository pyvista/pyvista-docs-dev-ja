import pyvista
from pyvista import examples
filename = examples.download_beach(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'beach.nrrd'
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh.plot()
