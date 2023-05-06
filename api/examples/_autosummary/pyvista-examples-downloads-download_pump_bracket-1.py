# Load the dataset.
#
import pyvista as pv
from pyvista import examples
dataset = examples.download_pump_bracket()
dataset  # doctest:+SKIP
# Expected:
## UnstructuredGrid (0x7f46a9279120)
##   N Cells:    124806
##   N Points:   250487
##   X Bounds:   -5.000e-01, 5.000e-01
##   Y Bounds:   -4.000e-01, 0.000e+00
##   Z Bounds:   -2.500e-02, 2.500e-02
##   N Arrays:   10
#
# Plot the displacement of the 4th mode shape as scalars.
#
cpos = [
    (0.744, -0.502, -0.830),
    (0.0520, -0.160, 0.0743),
    (-0.180, -0.958, 0.224),
]
dataset.plot(
    scalars='disp_3',
    cpos=cpos,
    show_scalar_bar=False,
    ambient=0.2,
    anti_aliasing='fxaa',
)
