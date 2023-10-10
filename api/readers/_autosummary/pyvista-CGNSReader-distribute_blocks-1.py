# Disable distributing blocks.
#
import pyvista as pv
from pyvista import examples
filename = examples.download_cgns_multi(load=False)
reader = pv.CGNSReader(filename)
reader.distribute_blocks = False
reader.distribute_blocks
# Expected:
## False
