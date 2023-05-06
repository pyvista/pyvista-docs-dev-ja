from pyvista import examples
mesh = examples.load_hexbeam()
cell = mesh.get_cell(0)
grid = cell.cast_to_unstructured_grid()
grid  # doctest: +SKIP
# Expected:
## UnstructuredGrid (0x7f9383619540)
##   N Cells:      1
##   N Points:     8
##   X Bounds:     0.000e+00, 5.000e-01
##   Y Bounds:     0.000e+00, 5.000e-01
##   Z Bounds:     0.000e+00, 5.000e-01
##   N Arrays:     0
