import pyvista as pv
from pyvista import examples
filename = examples.download_cavity(load=False)
reader = pv.OpenFOAMReader(filename)
reader.patch_array_names
# Expected:
## ['internalMesh', 'patch/movingWall', 'patch/fixedWalls', 'patch/frontAndBack']
