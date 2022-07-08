from pyvista import examples
mesh = examples.load_airplane()
mesh.cell_type(0)
# Expected:
## 5
#
# Cell type 5 is a triangular cell with three points.
#
mesh.cell_point_ids(0)
# Expected:
## [0, 1, 2]
