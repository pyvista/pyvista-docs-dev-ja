# Download and plot the dataset.
#
from pyvista import examples
mesh = examples.download_sea_vase()
mesh.plot()
#
# Return the statistics of the dataset.
#
mesh  # doctest:+SKIP
# Expected:
## PolyData (0x7fe8b3862460)
##   N Cells:      3548473
##   N Points:     1810012
##   X Bounds:     -1.666e+02, 1.465e+02
##   Y Bounds:     -1.742e+02, 1.384e+02
##   Z Bounds:     -1.500e+02, 2.992e+02
##   N Arrays:     0
