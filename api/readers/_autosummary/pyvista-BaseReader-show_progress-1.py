import pyvista as pv
from pyvista import examples
filename = examples.download_cavity(load=False)
reader = pv.OpenFOAMReader(filename)
reader.show_progress()
