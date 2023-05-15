# Download and plot the dataset.
#
from pyvista import examples
mesh = examples.download_bird_bath()
mesh.plot()
#
# Return the statistics of the dataset.
#
mesh
# Expected:
## PolyData (...)
##   N Cells:    3507935
##   N Points:   1831383
##   N Strips:   0
##   X Bounds:   -1.601e+02, 1.483e+02
##   Y Bounds:   -1.521e+02, 1.547e+02
##   Z Bounds:   -4.241e+00, 1.409e+02
##   N Arrays:   0
