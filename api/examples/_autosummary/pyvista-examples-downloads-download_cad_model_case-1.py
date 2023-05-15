# Download and plot the dataset.
#
from pyvista import examples
mesh = examples.download_cad_model_case()
mesh.plot()
#
# Return the statistics of the dataset.
#
mesh
# Expected:
## PolyData (...)
##   N Cells:    15446
##   N Points:   7677
##   N Strips:   0
##   X Bounds:   -6.460e-31, 9.000e+01
##   Y Bounds:   -3.535e-32, 1.480e+02
##   Z Bounds:   0.000e+00, 2.000e+01
##   N Arrays:   2
