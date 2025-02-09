# Validate an Nx3 array.
#
from pyvista import _validation
_validation.validate_arrayNx3(((1, 2, 3), (4, 5, 6)))
# Expected:
## array([[1, 2, 3],
##        [4, 5, 6]])
#
# One-dimensional 3-element arrays are automatically reshaped to 2D.
#
_validation.validate_arrayNx3([1, 2, 3])
# Expected:
## array([[1, 2, 3]])
#
# Add additional constraints.
#
_validation.validate_arrayNx3(
    ((1, 2, 3), (4, 5, 6)), must_be_in_range=[0, 10]
)
# Expected:
## array([[1, 2, 3],
##        [4, 5, 6]])
