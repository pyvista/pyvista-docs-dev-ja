import pyvista
from pyvista import examples
filename = examples.download_cavity(load=False)
reader = pyvista.OpenFOAMReader(filename)
reader.decompose_polyhedra = False
reader.decompose_polyhedra
# Expected:
## False
