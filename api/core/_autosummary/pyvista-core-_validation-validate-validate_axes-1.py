# Validate an axes array.
#
import numpy as np
from pyvista import _validation
_validation.validate_axes(np.eye(3))
# Expected:
## array([[1., 0., 0.],
##        [0., 1., 0.],
##        [0., 0., 1.]])
#
# Validate individual axes vectors as a 3x3 array.
#
_validation.validate_axes([1, 0, 0], [0, 1, 0], [0, 0, 1])
# Expected:
## array([[1., 0., 0.],
##        [0., 1., 0.],
##        [0., 0., 1.]])
#
# Create a validated left-handed axes array from two vectors.
#
_validation.validate_axes(
    [1, 0, 0], [0, 1, 0], must_have_orientation='left'
)
# Expected:
## array([[ 1.,  0.,  0.],
##        [ 0.,  1.,  0.],
##        [ 0.,  0., -1.]])
