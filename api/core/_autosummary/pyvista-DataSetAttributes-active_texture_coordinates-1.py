import pyvista as pv
mesh = pv.Cube()
mesh.point_data.active_texture_coordinates
# Expected:
## pyvista_ndarray([[ 0.,  0.],
##                  [ 1.,  0.],
##                  [ 1.,  1.],
##                  [ 0.,  1.],
##                  [-0.,  0.],
##                  [-0.,  1.],
##                  [-1.,  1.],
##                  [-1.,  0.]], dtype=float32)
