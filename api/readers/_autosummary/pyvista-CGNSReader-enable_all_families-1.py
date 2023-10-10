# Read all bases.
#
import pyvista as pv
from pyvista import examples
filename = examples.download_cgns_multi(load=False)
reader = pv.CGNSReader(filename)
reader.enable_all_families()
