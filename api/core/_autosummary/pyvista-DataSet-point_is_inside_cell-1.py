from pyvista import examples
mesh = examples.load_hexbeam()
mesh.get_cell(0).bounds
# Expected:
## BoundsTuple(x_min=0.0, x_max=0.5, y_min=0.0, y_max=0.5, z_min=0.0, z_max=0.5)
mesh.point_is_inside_cell(0, [0.2, 0.2, 0.2])
# Expected:
## True
