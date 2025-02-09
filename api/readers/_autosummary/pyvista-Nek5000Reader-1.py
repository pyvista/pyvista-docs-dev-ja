import pyvista as pv
from pyvista import examples
filename = examples.download_nek5000(load=False)
reader = pv.get_reader(filename)
mesh = reader.read()
mesh.plot(scalars='Velocity', cpos='xy')
