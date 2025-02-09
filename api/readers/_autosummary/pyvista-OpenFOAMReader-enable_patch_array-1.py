import pyvista as pv
from pyvista import examples
filename = examples.download_cavity(load=False)
reader = pv.OpenFOAMReader(filename)
reader.enable_patch_array('patch/movingWall')
reader.patch_array_status('patch/movingWall')
# Expected:
## True
