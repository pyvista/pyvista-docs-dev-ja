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
##   N Cells:    31366
##   N Points:   17337
##   N Strips:   0
##   X Bounds:   -1.091e+02, 1.533e+02
##   Y Bounds:   -1.200e+02, 1.416e+02
##   Z Bounds:   1.667e+01, 4.078e+02
##   N Arrays:   0
#
# .. seealso::
#
#     :ref:`Black Vase Dataset <black_vase_dataset>`
