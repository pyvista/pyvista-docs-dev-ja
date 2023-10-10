import pyvista as pv
from pyvista import examples
filename = examples.download_cavity(load=False)
reader = pv.POpenFOAMReader(filename)
reader.case_type = 'reconstructed'
reader.case_type
# Expected:
## 'reconstructed'
