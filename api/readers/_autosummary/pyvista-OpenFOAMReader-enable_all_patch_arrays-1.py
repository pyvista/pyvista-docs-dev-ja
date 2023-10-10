import pyvista as pv
from pyvista import examples
filename = examples.download_cavity(load=False)
reader = pv.OpenFOAMReader(filename)
reader.enable_all_patch_arrays()
assert reader.patch_array_status("patch/movingWall")
assert reader.patch_array_status("patch/fixedWalls")
