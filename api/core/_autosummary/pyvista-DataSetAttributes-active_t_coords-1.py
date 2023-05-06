import pyvista
mesh = pyvista.Cube()
mesh.point_data.active_t_coords
# Expected:
## pyvista_ndarray([[ 0.,  0.],
##                  [ 1.,  0.],
##                  [ 1.,  1.],
##                  [ 0.,  1.],
##                  [-0.,  0.],
##                  [-0.,  1.],
##                  [-1.,  1.],
##                  [-1.,  0.]], dtype=float32)
