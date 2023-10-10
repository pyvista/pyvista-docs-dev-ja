import pyvista as pv
from pyvista import examples
filename = examples.planets.download_mars_surface(load=False)
filename.split("/")[-1]  # omit the path
# Expected:
## 'mars.jpg'
reader = pv.get_reader(filename)
mesh = reader.read()
mesh.plot()
