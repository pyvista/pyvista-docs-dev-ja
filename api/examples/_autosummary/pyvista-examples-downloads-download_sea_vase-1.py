# Download and plot the dataset.
#
from pyvista import examples
mesh = examples.download_sea_vase()
mesh.plot()
#
# Return the statistics of the dataset.
#
mesh
# Expected:
## PolyData (...)
##   N Cells:    35483
##   N Points:   18063
##   N Strips:   0
##   X Bounds:   -1.664e+02, 1.463e+02
##   Y Bounds:   -1.741e+02, 1.382e+02
##   Z Bounds:   -1.497e+02, 2.992e+02
##   N Arrays:   0
#
# .. seealso::
#
#     :ref:`Sea Vase Dataset <sea_vase_dataset>`
