# Download and plot the dataset.
#
from pyvista import examples
mesh = examples.download_owl()
cpos = [
    (-315.18, -402.21, 230.71),
    (6.06, -1.74, 101.48),
    (0.108, 0.226, 0.968),
]
mesh.plot(cpos=cpos)
#
# Return the statistics of the dataset.
#
mesh
# Expected:
## PolyData (...)
##   N Cells:    24407
##   N Points:   12442
##   N Strips:   0
##   X Bounds:   -5.834e+01, 7.048e+01
##   Y Bounds:   -7.005e+01, 6.657e+01
##   Z Bounds:   1.814e+00, 2.013e+02
##   N Arrays:   0
#
# .. seealso::
#
#     :ref:`Owl Dataset <owl_dataset>`
