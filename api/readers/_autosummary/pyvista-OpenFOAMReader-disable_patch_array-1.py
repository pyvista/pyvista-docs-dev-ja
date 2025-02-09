import pyvista as pv
from pyvista import examples
filename = examples.download_cavity(load=False)
reader = pv.OpenFOAMReader(filename)
reader.disable_patch_array('internalMesh')
reader.patch_array_status('internalMesh')
# Expected:
## False
