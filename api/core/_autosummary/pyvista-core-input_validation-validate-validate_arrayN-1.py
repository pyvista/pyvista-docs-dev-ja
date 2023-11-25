# Validate a 1D array with four elements.
#
import pyvista.core.input_validation as valid
valid.validate_arrayN((1, 2, 3, 4))
# Expected:
## array([1, 2, 3, 4])
#
# Scalar 0-dimensional values are automatically reshaped to be 1D.
#
valid.validate_arrayN(42.0)
# Expected:
## array([42.0])
#
# 2D arrays where the first dimension is unity are automatically
# reshaped to be 1D.
#
valid.validate_arrayN([[1, 2]])
# Expected:
## array([1, 2])
#
# Add additional constraints if needed.
#
valid.validate_arrayN((1, 2, 3), must_have_length=3)
# Expected:
## array([1, 2, 3])
