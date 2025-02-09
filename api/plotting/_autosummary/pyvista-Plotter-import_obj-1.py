import pyvista as pv
from pyvista import examples
download_obj_file = examples.download_room_surface_mesh(load=False)
pl = pv.Plotter()
pl.import_obj(download_obj_file)
pl.show()
#
# Import an .obj file with a texture.
#
from pathlib import Path
filename = examples.download_doorman(load=False)
pl = pv.Plotter()
pl.import_obj(filename)
pl.show(cpos='xy')
