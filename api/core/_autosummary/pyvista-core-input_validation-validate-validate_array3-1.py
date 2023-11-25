# Validate a 1D array with three elements.
#
import pyvista.core.input_validation as valid
valid.validate_array3((1, 2, 3))
# Expected:
## array([1, 2, 3])
#
# 2D 3-element arrays are automatically reshaped to be 1D.
#
valid.validate_array3([[1, 2, 3]])
# Expected:
## array([1, 2, 3])
#
# Scalar 0-dimensional values can be automatically broadcast as
# a 3-element 1D array.
#
valid.validate_array3(42.0, broadcast=True)
# Expected:
## array([42.0, 42.0, 42.0])
#
# Add additional constraints if needed.
#
valid.validate_array3((1, 2, 3), must_be_nonnegative=True)
# Expected:
## array([1, 2, 3])
