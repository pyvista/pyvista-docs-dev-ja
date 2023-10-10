import pyvista as pv
from pyvista import examples
filename = examples.download_parched_canal_4k(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'parched_canal_4k.hdr'
reader = pv.get_reader(filename)
mesh = reader.read()
mesh.plot()
