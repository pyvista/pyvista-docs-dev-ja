# Set adding an empty physical dimension to vectors to ``True``.
#
import pyvista as pv
from pyvista import examples
filename = examples.download_cgns_multi(load=False)
reader = pv.CGNSReader(filename)
reader.vector_3d = True
reader.vector_3d
# Expected:
## True
