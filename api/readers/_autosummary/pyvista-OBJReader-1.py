import pyvista as pv
from pyvista import examples
filename = examples.download_trumpet(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'trumpet.obj'
reader = pv.get_reader(filename)
mesh = reader.read()
mesh.plot(cpos='yz', show_scalar_bar=False)
