import pyvista as pv
from pyvista import examples
filename = examples.download_room_cff(load=False)
reader = pv.get_reader(filename)
blocks = reader.read()
mesh = blocks[0]
mesh.plot(cpos='xy', scalars='SV_T')
