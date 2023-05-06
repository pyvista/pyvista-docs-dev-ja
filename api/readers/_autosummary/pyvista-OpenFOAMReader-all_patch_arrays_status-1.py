import pyvista
from pyvista import examples
filename = examples.download_cavity(load=False)
reader = pyvista.OpenFOAMReader(filename)
reader.all_patch_arrays_status  # doctest: +NORMALIZE_WHITESPACE
# Expected:
## {'internalMesh': True, 'patch/movingWall': True, 'patch/fixedWalls': True,
##  'patch/frontAndBack': True}
