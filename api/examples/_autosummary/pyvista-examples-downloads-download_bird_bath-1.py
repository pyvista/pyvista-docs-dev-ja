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
##   N Cells:    35079
##   N Points:   18796
##   N Strips:   0
##   X Bounds:   -1.600e+02, 1.482e+02
##   Y Bounds:   -1.522e+02, 1.547e+02
##   Z Bounds:   -5.491e-01, 1.408e+02
##   N Arrays:   0
#
# .. seealso::
#
#     :ref:`Bird Bath Dataset <bird_bath_dataset>`
