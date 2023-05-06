# Disable distributing blocks.
#
import pyvista
from pyvista import examples
filename = examples.download_cgns_multi(load=False)
reader = pyvista.CGNSReader(filename)
reader.distribute_blocks = False
reader.distribute_blocks
# Expected:
## False
