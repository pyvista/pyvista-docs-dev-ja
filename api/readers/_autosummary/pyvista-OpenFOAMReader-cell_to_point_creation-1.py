import pyvista as pv
from pyvista import examples
filename = examples.download_cavity(load=False)
reader = pv.OpenFOAMReader(filename)
reader.cell_to_point_creation = False
reader.cell_to_point_creation
# Expected:
## False
