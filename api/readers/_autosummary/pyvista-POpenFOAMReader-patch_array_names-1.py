import pyvista
from pyvista import examples
filename = examples.download_cavity(load=False)
reader = pyvista.OpenFOAMReader(filename)
reader.patch_array_names
# Expected:
## ['internalMesh', 'patch/movingWall', 'patch/fixedWalls', 'patch/frontAndBack']
