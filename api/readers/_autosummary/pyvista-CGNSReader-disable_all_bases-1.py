# Disable reading all bases.
#
import pyvista as pv
from pyvista import examples
filename = examples.download_cgns_multi(load=False)
reader = pv.CGNSReader(filename)
reader.disable_all_bases()
