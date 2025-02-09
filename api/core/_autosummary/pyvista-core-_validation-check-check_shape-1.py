# Check if an array is one-dimensional.
#
import numpy as np
from pyvista import _validation
_validation.check_shape([1, 2, 3], shape=(-1))
#
# Check if an array is one-dimensional or a scalar.
#
_validation.check_shape(1, shape=[(), (-1)])
#
# Check if an array is 3x3 or 4x4.
#
_validation.check_shape(np.eye(3), shape=[(3, 3), (4, 4)])
