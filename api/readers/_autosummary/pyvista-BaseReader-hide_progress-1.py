import pyvista
from pyvista import examples
filename = examples.download_cavity(load=False)
reader = pyvista.OpenFOAMReader(filename)
reader.hide_progress()
