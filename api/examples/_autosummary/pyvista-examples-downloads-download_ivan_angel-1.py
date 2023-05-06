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
mesh  # doctest:+SKIP
# Expected:
## PolyData (0x7f6ed1345520)
##   N Cells:      4547716
##   N Points:     2297089
##   X Bounds:     -1.147e+02, 8.468e+01
##   Y Bounds:     -7.103e+01, 9.247e+01
##   Z Bounds:     -1.198e+02, 2.052e+02
##   N Arrays:     0
