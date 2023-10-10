import pyvista as pv
mesh = pv.Cube()
mesh.clear_data()
mesh.cell_data['data0'] = [0] * mesh.n_cells
mesh.cell_data['data1'] = range(mesh.n_cells)
mesh.cell_data.items()
# Expected:
## [('data0', pyvista_ndarray([0, 0, 0, 0, 0, 0])), ('data1', pyvista_ndarray([0, 1, 2, 3, 4, 5]))]
