# Enable loading boundary patches .
#
import pyvista as pv
from pyvista import examples
filename = examples.download_cgns_multi(load=False)
reader = pv.CGNSReader(filename)
reader.load_boundary_patch = True
reader.load_boundary_patch
# Expected:
## True
