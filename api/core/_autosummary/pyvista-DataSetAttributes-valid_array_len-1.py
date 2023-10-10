# Show that valid array lengths match the number of points and
# cells for point and cell arrays, and there is no length limit
# for field data.
#
import pyvista as pv
mesh = pv.Cube()
mesh.n_points, mesh.n_cells
# Expected:
## (8, 6)
mesh.point_data.valid_array_len
# Expected:
## 8
mesh.cell_data.valid_array_len
# Expected:
## 6
mesh.field_data.valid_array_len is None
# Expected:
## True
