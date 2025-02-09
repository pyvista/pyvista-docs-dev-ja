import pyvista as pv
from pyvista import examples
filename = examples.download_prism(load=False)
reader = pv.get_reader(filename)
mesh = reader.read()
mesh.plot()
