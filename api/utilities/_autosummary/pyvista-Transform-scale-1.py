# Compose a scale matrix.
#
import pyvista as pv
transform = pv.Transform().scale(1, 2, 3)
transform.matrix
# Expected:
## array([[1., 0., 0., 0.],
##        [0., 2., 0., 0.],
##        [0., 0., 3., 0.],
##        [0., 0., 0., 1.]])
#
# Compose a second scale matrix using ``*``.
#
transform = transform * 2
transform.matrix
# Expected:
## array([[2., 0., 0., 0.],
##        [0., 4., 0., 0.],
##        [0., 0., 6., 0.],
##        [0., 0., 0., 1.]])
#
# Scale from a point. Check the :attr:`matrix_list` to see that a translation
# is added before and after the scaling.
#
transform = pv.Transform().scale(7, point=(1, 2, 3))
translation_to_origin = transform.matrix_list[0]
translation_to_origin
# Expected:
## array([[ 1.,  0.,  0., -1.],
##        [ 0.,  1.,  0., -2.],
##        [ 0.,  0.,  1., -3.],
##        [ 0.,  0.,  0.,  1.]])
#
scale = transform.matrix_list[1]
scale
# Expected:
## array([[7., 0., 0., 0.],
##        [0., 7., 0., 0.],
##        [0., 0., 7., 0.],
##        [0., 0., 0., 1.]])
#
translation_from_origin = transform.matrix_list[2]
translation_from_origin
# Expected:
## array([[1., 0., 0., 1.],
##        [0., 1., 0., 2.],
##        [0., 0., 1., 3.],
##        [0., 0., 0., 1.]])
