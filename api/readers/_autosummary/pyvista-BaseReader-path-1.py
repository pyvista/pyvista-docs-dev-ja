import pyvista as pv
from pyvista import examples
filename = examples.download_human(load=False)
reader = pv.XMLPolyDataReader(filename)
reader.path  # doctest:+SKIP
# Expected:
## '/home/user/.local/share/pyvista/examples/Human.vtp'
