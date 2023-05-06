# Download and plot the dataset.
#
from pyvista import examples
mesh = examples.download_plastic_vase()
mesh.plot()
#
# Return the statistics of the dataset.
#
mesh  # doctest:+SKIP
# Expected:
## PolyData (0x7fe8cadc14c0)
##   N Cells:      3570967
##   N Points:     1796805
##   X Bounds:     -1.364e+02, 1.929e+02
##   Y Bounds:     -1.677e+02, 1.603e+02
##   Z Bounds:     1.209e+02, 4.090e+02
##   N Arrays:     0
