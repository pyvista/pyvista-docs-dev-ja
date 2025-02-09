# Validate a rotation matrix. The identity matrix is used as a toy example.
#
import numpy as np
from pyvista import _validation
rotation = np.eye(3)
_validation.validate_rotation(rotation)
# Expected:
## array([[1., 0., 0.],
##        [0., 1., 0.],
##        [0., 0., 1.]])
#
# By default, left-handed rotations (which include reflections) are allowed.
#
rotation *= -1  # Add reflections
_validation.validate_rotation(rotation)
# Expected:
## array([[-1., -0., -0.],
##        [-0., -1., -0.],
##        [-0., -0., -1.]])
