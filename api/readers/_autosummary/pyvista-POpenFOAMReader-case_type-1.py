import pyvista
from pyvista import examples
filename = examples.download_cavity(load=False)
reader = pyvista.POpenFOAMReader(filename)
reader.case_type = 'reconstructed'
reader.case_type
# Expected:
## 'reconstructed'
