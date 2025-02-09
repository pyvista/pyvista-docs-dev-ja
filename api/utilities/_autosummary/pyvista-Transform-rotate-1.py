# Compose a rotation matrix. In this case the rotation rotates about the
# z-axis by 90 degrees.
#
import pyvista as pv
rotation_z_90 = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
transform = pv.Transform().rotate(rotation_z_90)
transform.matrix
# Expected:
## array([[ 0., -1.,  0.,  0.],
##        [ 1.,  0.,  0.,  0.],
##        [ 0.,  0.,  1.,  0.],
##        [ 0.,  0.,  0.,  1.]])
#
# Compose a second rotation matrix. In this case we use the same rotation as
# before.
#
_ = transform.rotate(rotation_z_90)
#
# The result is a matrix that rotates about the z-axis by 180 degrees.
#
transform.matrix
# Expected:
## array([[-1.,  0.,  0.,  0.],
##        [ 0., -1.,  0.,  0.],
##        [ 0.,  0.,  1.,  0.],
##        [ 0.,  0.,  0.,  1.]])
#
# Rotate about a point. Check the :attr:`matrix_list` to see that a translation
# is added before and after the rotation.
#
transform = pv.Transform().rotate(rotation_z_90, point=(1, 2, 3))
translation_to_origin = transform.matrix_list[0]
translation_to_origin
# Expected:
## array([[ 1.,  0.,  0., -1.],
##        [ 0.,  1.,  0., -2.],
##        [ 0.,  0.,  1., -3.],
##        [ 0.,  0.,  0.,  1.]])
#
rotation = transform.matrix_list[1]
rotation
# Expected:
## array([[ 0., -1.,  0.,  0.],
##        [ 1.,  0.,  0.,  0.],
##        [ 0.,  0.,  1.,  0.],
##        [ 0.,  0.,  0.,  1.]])
#
translation_from_origin = transform.matrix_list[2]
translation_from_origin
# Expected:
## array([[1., 0., 0., 1.],
##        [0., 1., 0., 2.],
##        [0., 0., 1., 3.],
##        [0., 0., 0., 1.]])
