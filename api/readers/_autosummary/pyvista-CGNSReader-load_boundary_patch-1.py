# Enable loading boundary patches .
#
import pyvista
from pyvista import examples
filename = examples.download_cgns_multi(load=False)
reader = pyvista.CGNSReader(filename)
reader.load_boundary_patch = True
reader.load_boundary_patch
# Expected:
## True
