from pyvista import examples
grid = examples.load_explicit_structured()
grid = grid.hide_cells(range(80, 120))
grid.bounds
# Expected:
## (0.0, 80.0, 0.0, 50.0, 0.0, 6.0)
#
grid.visible_bounds
# Expected:
## (0.0, 80.0, 0.0, 50.0, 0.0, 4.0)
