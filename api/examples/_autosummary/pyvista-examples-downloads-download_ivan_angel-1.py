# Download and plot the dataset.
#
from pyvista import examples
mesh = examples.download_ivan_angel()
cpos = [
    (-476.14, -393.73, 282.14),
    (-15.00, 11.25, 44.08),
    (0.26, 0.24, 0.93),
]
mesh.plot(cpos=cpos)
#
# Return the statistics of the dataset.
#
mesh
# Expected:
## PolyData (...)
##   N Cells:    35804
##   N Points:   18412
##   N Strips:   0
##   X Bounds:   -1.146e+02, 8.470e+01
##   Y Bounds:   -6.987e+01, 9.254e+01
##   Z Bounds:   -1.166e+02, 2.052e+02
##   N Arrays:   0
#
# .. seealso::
#
#     :ref:`Ivan Angel Dataset <ivan_angel_dataset>`
