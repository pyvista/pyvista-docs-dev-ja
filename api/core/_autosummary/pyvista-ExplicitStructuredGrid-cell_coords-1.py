from pyvista import examples
grid = examples.load_explicit_structured()
grid.cell_coords(19)
# Expected:
## array([3, 4, 0])
#
grid.cell_coords((19, 31, 41, 54))
# Expected:
## array([[3, 4, 0],
##        [3, 2, 1],
##        [1, 0, 2],
##        [2, 3, 2]])
