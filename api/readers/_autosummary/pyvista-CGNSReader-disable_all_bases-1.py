# Disable reading all bases.
#
import pyvista
from pyvista import examples
filename = examples.download_cgns_multi(load=False)
reader = pyvista.CGNSReader(filename)
reader.disable_all_bases()
