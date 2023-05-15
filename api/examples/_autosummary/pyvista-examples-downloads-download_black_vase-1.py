# Download and plot the dataset.
#
from pyvista import examples
mesh = examples.download_black_vase()
mesh.plot()
#
# Return the statistics of the dataset.
#
mesh
# Expected:
## PolyData (...)
##   N Cells:    3136652
##   N Points:   1611789
##   N Strips:   0
##   X Bounds:   -1.092e+02, 1.533e+02
##   Y Bounds:   -1.200e+02, 1.415e+02
##   Z Bounds:   1.666e+01, 4.077e+02
##   N Arrays:   0
