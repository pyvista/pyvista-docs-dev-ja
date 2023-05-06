# Create an actor and assign a mapper to it.
#
import pyvista as pv
dataset = pv.Sphere()
actor = pv.Actor()
actor.mapper = pv.DataSetMapper(dataset)
actor.mapper  # doctest:+SKIP
# Expected:
## DataSetMapper (0x7f34dcec5040)
##   Scalar visibility:           True
##   Scalar range:                (0.0, 1.0)
##   Interpolate before mapping:  False
##   Scalar map mode:             default
##   Color mode:                  direct
## <BLANKLINE>
## Attached dataset:
## PolyData (0x7f34dcec5f40)
##   N Cells:  1680
##   N Points: 842
##   N Strips: 0
##   X Bounds: -4.993e-01, 4.993e-01
##   Y Bounds: -4.965e-01, 4.965e-01
##   Z Bounds: -5.000e-01, 5.000e-01
##   N Arrays: 1
## <BLANKLINE>
