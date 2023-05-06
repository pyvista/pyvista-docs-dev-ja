import pyvista
from pyvista import examples
filename = examples.download_gourds_pnm(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'Gourds.pnm'
reader = pyvista.get_reader(filename)
mesh = reader.read()
mesh.plot()
