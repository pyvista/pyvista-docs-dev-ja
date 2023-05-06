# Download and plot the dataset.
#
from pyvista import examples
mesh = examples.download_cad_model_case()
mesh.plot()
#
# Return the statistics of the dataset.
#
mesh  # doctest:+SKIP
# Expected:
## PolyData (0x7fd08f1faf40)
##   N Cells:      13702
##   N Points:     6801
##   X Bounds:     -6.460e-31, 9.000e+01
##   Y Bounds:     -3.535e-32, 1.480e+02
##   Z Bounds:     -7.287e-13, 2.000e+01
##   N Arrays:     1
