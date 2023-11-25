# Validate a number.
#
import pyvista.core.input_validation as valid
valid.validate_number(1)
# Expected:
## 1
#
# 1D arrays are automatically reshaped.
#
valid.validate_number([42.0])
# Expected:
## 42.0
#
# Additional checks can be added as needed.
#
valid.validate_number(
    10, must_be_in_range=[0, 10], must_be_integer_like=True
)
# Expected:
## 10
