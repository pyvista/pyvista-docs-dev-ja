import pyvista as pv
mesh = pv.Cube()
index = mesh.find_cells_within_bounds([-2.0, 2.0, -2.0, 2.0, -2.0, 2.0])
