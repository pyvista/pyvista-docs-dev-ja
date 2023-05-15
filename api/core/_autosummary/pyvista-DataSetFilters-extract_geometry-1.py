# Extract the surface of a sample unstructured grid.
#
import pyvista
from pyvista import examples
hex_beam = pyvista.read(examples.hexbeamfile)
hex_beam.extract_geometry()
# Expected:
## PolyData (...)
##   N Cells:    88
##   N Points:   90
##   N Strips:   0
##   X Bounds:   0.000e+00, 1.000e+00
##   Y Bounds:   0.000e+00, 1.000e+00
##   Z Bounds:   0.000e+00, 5.000e+00
##   N Arrays:   3
