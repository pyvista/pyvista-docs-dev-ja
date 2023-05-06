import pyvista
from pyvista import examples
filename = examples.download_cavity(load=False)
reader = pyvista.OpenFOAMReader(filename)
reader.enable_patch_array("patch/movingWall")
reader.patch_array_status("patch/movingWall")
# Expected:
## True
