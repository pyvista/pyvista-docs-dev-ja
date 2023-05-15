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
##   N Cells:    3580454
##   N Points:   1811531
##   N Strips:   0
##   X Bounds:   -1.147e+02, 8.468e+01
##   Y Bounds:   -6.996e+01, 9.247e+01
##   Z Bounds:   -1.171e+02, 2.052e+02
##   N Arrays:   0
