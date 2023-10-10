# Add a point array to a mesh.
#
import pyvista as pv
mesh = pv.Cube()
data = range(mesh.n_points)
mesh.point_data.set_array(data, 'my-data')
mesh.point_data['my-data']
# Expected:
## pyvista_ndarray([0, 1, 2, 3, 4, 5, 6, 7])
#
# Add a cell array to a mesh.
#
cell_data = range(mesh.n_cells)
mesh.cell_data.set_array(cell_data, 'my-data')
mesh.cell_data['my-data']
# Expected:
## pyvista_ndarray([0, 1, 2, 3, 4, 5])
#
# Add field data to a mesh.
#
field_data = range(3)
mesh.field_data.set_array(field_data, 'my-data')
mesh.field_data['my-data']
# Expected:
## pyvista_ndarray([0, 1, 2])
