import pyvista as pv
mesh = pv.Cube()
mesh.point_data.active_t_coords_name
# Expected:
## 'TCoords'
