# Download and plot the dataset.
#
from pyvista import examples
mesh = examples.download_plastic_vase()
mesh.plot()
#
# Return the statistics of the dataset.
#
mesh
# Expected:
## PolyData (...)
##   N Cells:    35708
##   N Points:   18238
##   N Strips:   0
##   X Bounds:   -1.364e+02, 1.928e+02
##   Y Bounds:   -1.677e+02, 1.602e+02
##   Z Bounds:   1.209e+02, 4.090e+02
##   N Arrays:   0
#
# .. seealso::
#
#     :ref:`Plastic Vase Dataset <plastic_vase_dataset>`
