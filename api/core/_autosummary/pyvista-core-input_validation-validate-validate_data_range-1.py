# Validate a data range.
#
import pyvista.core.input_validation as valid
valid.validate_data_range([-5, 5])
# Expected:
## (-5, 5)
#
# Add additional constraints if needed.
#
valid.validate_data_range([0, 1.0], must_be_nonnegative=True)
# Expected:
## (0.0, 1.0)
