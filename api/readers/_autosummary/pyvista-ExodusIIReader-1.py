import pyvista as pv
from pyvista import examples
filename = examples.download_mug(load=False)
reader = pv.get_reader(filename)
mesh = reader.read()
mesh.plot()
