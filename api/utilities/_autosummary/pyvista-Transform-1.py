# Create a transformation and use ``+`` to compose a translation.
#
import numpy as np
import pyvista as pv
position = (-0.6, -0.8, 2.1)
translation_T = pv.Transform() + position
translation_T.matrix
# Expected:
## array([[ 1. ,  0. ,  0. , -0.6],
##        [ 0. ,  1. ,  0. , -0.8],
##        [ 0. ,  0. ,  1. ,  2.1],
##        [ 0. ,  0. ,  0. ,  1. ]])
#
# Using ``+`` performs the same concatenation as calling :meth:`translate`.
#
np.array_equal(
    translation_T.matrix, pv.Transform().translate(position).matrix
)
# Expected:
## True
#
# Create a transformation and use ``*`` to compose a scaling matrix.
#
scale_factor = 2.0
scaling_T = pv.Transform() * scale_factor
scaling_T.matrix
# Expected:
## array([[2., 0., 0., 0.],
##        [0., 2., 0., 0.],
##        [0., 0., 2., 0.],
##        [0., 0., 0., 1.]])
#
# Using ``*`` performs the same concatenation as calling :meth:`scale`.
#
np.array_equal(scaling_T.matrix, pv.Transform().scale(scale_factor).matrix)
# Expected:
## True
#
# Compose the two transformations using ``*``. This will compose with
# post-multiplication such that the transformations are applied in order from left to
# right, i.e. translate first, then scale.
#
transform_post = translation_T * scaling_T
transform_post.matrix
# Expected:
## array([[ 2. ,  0. ,  0. , -1.2],
##        [ 0. ,  2. ,  0. , -1.6],
##        [ 0. ,  0. ,  2. ,  4.2],
##        [ 0. ,  0. ,  0. ,  1. ]])
#
# Post-multiplication is equivalent to using matrix multiplication on the
# arrays directly but with the arguments reversed:
#
mat_mul = scaling_T.matrix @ translation_T.matrix
np.array_equal(transform_post.matrix, mat_mul)
# Expected:
## True
#
# Alternatively, compose the transformations by chaining the methods with a
# single :class:`Transform` instance. Note that post-multiply is used by default.
#
transform_post = pv.Transform()
transform_post.multiply_mode
# Expected:
## 'post'
_ = transform_post.translate(position).scale(scale_factor)
transform_post.matrix
# Expected:
## array([[ 2. ,  0. ,  0. , -1.2],
##        [ 0. ,  2. ,  0. , -1.6],
##        [ 0. ,  0. ,  2. ,  4.2],
##        [ 0. ,  0. ,  0. ,  1. ]])
#
# Use :attr:`n_transformations` to check that there are two transformations.
#
transform_post.n_transformations
# Expected:
## 2
#
# Use :attr:`matrix_list` to get a list of the transformations. Since
# post-multiplication is used, the translation matrix is first in the list since
# it was applied first, and the scale matrix is second.
#
transform_post.matrix_list[0]  # translation
# Expected:
## array([[ 1. ,  0. ,  0. , -0.6],
##        [ 0. ,  1. ,  0. , -0.8],
##        [ 0. ,  0. ,  1. ,  2.1],
##        [ 0. ,  0. ,  0. ,  1. ]])
#
transform_post.matrix_list[1]  # scaling
# Expected:
## array([[2., 0., 0., 0.],
##        [0., 2., 0., 0.],
##        [0., 0., 2., 0.],
##        [0., 0., 0., 1.]])
#
# Create a similar transform but use pre-multiplication this time. Compose the
# transformations in the same order as before using :meth:`translate` and :meth:`scale`.
#
transform_pre = pv.Transform().pre_multiply()
_ = transform_pre.translate(position).scale(scale_factor)
#
# This is equivalent to using matrix multiplication directly on the arrays:
#
mat_mul = translation_T.matrix @ scaling_T.matrix
np.array_equal(transform_pre.matrix, mat_mul)
# Expected:
## True
#
# Show the matrix list again. Note how the order with pre-multiplication is the
# reverse of post-multiplication.
#
transform_pre.matrix_list[0]  # scaling
# Expected:
## array([[2., 0., 0., 0.],
##        [0., 2., 0., 0.],
##        [0., 0., 2., 0.],
##        [0., 0., 0., 1.]])
#
transform_pre.matrix_list[1]  # translation
# Expected:
## array([[ 1. ,  0. ,  0. , -0.6],
##        [ 0. ,  1. ,  0. , -0.8],
##        [ 0. ,  0. ,  1. ,  2.1],
##        [ 0. ,  0. ,  0. ,  1. ]])
#
# Apply the two post- and pre-multiplied transformations to a dataset and plot them.
# Note how the meshes have different positions since post- and pre-multiplication
# produce different transformations.
#
mesh_post = pv.Sphere().transform(transform_post, inplace=False)
mesh_pre = pv.Cone().transform(transform_pre, inplace=False)
pl = pv.Plotter()
_ = pl.add_mesh(mesh_post, color='goldenrod')
_ = pl.add_mesh(mesh_pre, color='teal')
_ = pl.add_axes_at_origin()
pl.show()
#
# Get the composed inverse transformation matrix of the pre-multiplication case.
#
inverse_matrix = transform_pre.inverse_matrix
inverse_matrix
# Expected:
## array([[ 0.5 ,  0.  ,  0.  ,  0.3 ],
##        [ 0.  ,  0.5 ,  0.  ,  0.4 ],
##        [ 0.  ,  0.  ,  0.5 , -1.05],
##        [ 0.  ,  0.  ,  0.  ,  1.  ]])
#
# Similar to using :attr:`matrix_list`, we can inspect the individual transformation
# inverses with :attr:`inverse_matrix_list`.
#
transform_pre.inverse_matrix_list[0]  # inverse scaling
# Expected:
## array([[0.5, 0. , 0. , 0. ],
##        [0. , 0.5, 0. , 0. ],
##        [0. , 0. , 0.5, 0. ],
##        [0. , 0. , 0. , 1. ]])
#
transform_pre.inverse_matrix_list[1]  # inverse translation
# Expected:
## array([[ 1. ,  0. ,  0. ,  0.6],
##        [ 0. ,  1. ,  0. ,  0.8],
##        [ 0. ,  0. ,  1. , -2.1],
##        [ 0. ,  0. ,  0. ,  1. ]])
#
# Transform the mesh by its inverse to restore it to its original un-scaled state
# and positioning at the origin.
#
mesh_pre_inverted = mesh_pre.transform(inverse_matrix, inplace=False)
pl = pv.Plotter()
_ = pl.add_mesh(mesh_pre_inverted, color='teal')
_ = pl.add_axes_at_origin()
pl.show()
