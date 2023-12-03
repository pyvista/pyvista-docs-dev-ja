from pyvista import examples
mesh = examples.load_sphere()
cell = mesh.get_cell(0)
grid = cell.cast_to_polydata()
grid  # doctest: +SKIP
# Expected:
## PolyData (0x7f09ae437b80)
##   N Cells:    1
##   N Points:   3
##   N Strips:   0
##    X Bounds:   0.000e+00, 1.000e+01
##   Y Bounds:   0.000e+00, 2.500e+01
##   Z Bounds:   -1.270e+02, -1.250e+02
##   N Arrays:   0
