import pyvista
mesh = pyvista.Cube()
mesh.point_data.active_t_coords_name
# Expected:
## 'TCoords'
