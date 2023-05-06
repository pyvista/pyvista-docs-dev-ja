import pyvista
from pyvista import examples
filename = examples.download_st_helens(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'SainteHelens.dem'
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh.plot()
