# Validate a dimensionality.
#
from pyvista import _validation
_validation.validate_dimensionality('1D')
# Expected:
## 1
#
# 1D arrays are automatically reshaped.
#
_validation.validate_dimensionality([3])
# Expected:
## 3
