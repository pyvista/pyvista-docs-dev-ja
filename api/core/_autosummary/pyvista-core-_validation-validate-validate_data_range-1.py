# Validate a data range.
#
from pyvista import _validation
_validation.validate_data_range([-5, 5])
# Expected:
## (-5, 5)
#
# Add additional constraints if needed.
#
_validation.validate_data_range([0, 1.0], must_be_nonnegative=True)
# Expected:
## (0.0, 1.0)
