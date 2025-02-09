import pyvista as pv
from pyvista import examples
blocks = examples.download_room_cff()
mesh = blocks[0]
mesh.plot(cpos='xy', scalars='SV_T')
#
# .. seealso::
#
#     :ref:`Room Cff Dataset <room_cff_dataset>`
