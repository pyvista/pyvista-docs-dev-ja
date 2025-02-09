import pyvista as pv
from pyvista import examples
filename = examples.download_t3_grid_0(load=False)
reader = pv.get_reader(filename)
mesh = reader.read()
mesh.plot()
