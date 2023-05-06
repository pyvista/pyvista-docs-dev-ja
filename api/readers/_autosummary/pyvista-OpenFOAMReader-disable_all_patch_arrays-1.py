import pyvista
from pyvista import examples
filename = examples.download_cavity(load=False)
reader = pyvista.OpenFOAMReader(filename)
reader.disable_all_patch_arrays()
assert not reader.patch_array_status("patch.movingWall")
assert not reader.patch_array_status("internalMesh")
