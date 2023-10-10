import pyvista as pv
from pyvista import examples
filename = examples.download_cavity(load=False)
reader = pv.OpenFOAMReader(filename)
reader.skip_zero_time = False
reader.skip_zero_time
# Expected:
## False
