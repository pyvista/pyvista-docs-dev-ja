import pyvista as pv
from pyvista import examples
filename = examples.download_cavity(load=False)
reader = pv.OpenFOAMReader(filename)
reader.decompose_polyhedra = False
reader.decompose_polyhedra
# Expected:
## False
