# Validate an Nx3 array.
#
import pyvista.core.input_validation as valid
valid.validate_arrayNx3(((1, 2, 3), (4, 5, 6)))
# Expected:
## array([[1, 2, 3],
##        [4, 5, 6]])
#
# One-dimensional 3-element arrays are automatically reshaped to 2D.
#
valid.validate_arrayNx3([1, 2, 3])
# Expected:
## array([[1, 2, 3]])
#
# Add additional constraints.
#
valid.validate_arrayNx3(
    ((1, 2, 3), (4, 5, 6)), must_be_in_range=[0, 10]
)
# Expected:
## array([[1, 2, 3],
##        [4, 5, 6]])
