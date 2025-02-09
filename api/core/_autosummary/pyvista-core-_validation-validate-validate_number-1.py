# Validate a number.
#
from pyvista import _validation
_validation.validate_number(1)
# Expected:
## 1
#
# 1D arrays are automatically reshaped.
#
_validation.validate_number([42.0])
# Expected:
## 42.0
#
# Additional checks can be added as needed.
#
_validation.validate_number(
    10, must_be_in_range=[0, 10], must_be_integer=True
)
# Expected:
## 10
