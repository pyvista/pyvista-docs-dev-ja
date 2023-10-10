# Set reading the unsteady pattern to ``True``.
#
import pyvista as pv
from pyvista import examples
filename = examples.download_cgns_multi(load=False)
reader = pv.CGNSReader(filename)
reader.unsteady_pattern = True
reader.unsteady_pattern
# Expected:
## True
