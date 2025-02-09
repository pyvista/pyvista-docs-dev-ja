import pyvista as pv
from pyvista import examples
filename = examples.download_e07733s002i009(load=False)
reader = pv.get_reader(filename)
mesh = reader.read()
mesh.plot()
