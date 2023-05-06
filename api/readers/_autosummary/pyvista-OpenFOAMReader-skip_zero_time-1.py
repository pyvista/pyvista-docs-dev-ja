import pyvista
from pyvista import examples
filename = examples.download_cavity(load=False)
reader = pyvista.OpenFOAMReader(filename)
reader.skip_zero_time = False
reader.skip_zero_time
# Expected:
## False
