from pyvista import examples
grid = examples.load_explicit_structured()
grid = grid.hide_cells(range(80, 120))
grid.bounds
# Expected:
## BoundsTuple(x_min=0.0, x_max=80.0, y_min=0.0, y_max=50.0, z_min=0.0, z_max=6.0)
#
grid.visible_bounds
# Expected:
## BoundsTuple(x_min=0.0, x_max=80.0, y_min=0.0, y_max=50.0, z_min=0.0, z_max=4.0)
