# Validate a 1D array with four non-negative integer-like elements.
#
import numpy as np
from pyvista import _validation
arr = _validation.validate_arrayN_unsigned((1.0, 2.0, 3.0, 4.0))
arr
# Expected:
## array([1, 2, 3, 4])
#
# Verify that the output data type is integral.
#
np.issubdtype(arr.dtype, int)
# Expected:
## True
#
# Scalar 0-dimensional values are automatically reshaped to be 1D.
#
_validation.validate_arrayN_unsigned(42)
# Expected:
## array([42])
#
# 2D arrays where the first dimension is unity are automatically
# reshaped to be 1D.
#
_validation.validate_arrayN_unsigned([[1, 2]])
# Expected:
## array([1, 2])
#
# Add additional constraints if needed.
#
_validation.validate_arrayN_unsigned((1, 2, 3), must_be_in_range=[1, 3])
# Expected:
## array([1, 2, 3])
