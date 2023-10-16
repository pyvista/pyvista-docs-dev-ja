import pyvista as pv
mesh = pv.Cube()
mesh.point_data.active_texture_coordinates_name
# Expected:
## 'TCoords'
