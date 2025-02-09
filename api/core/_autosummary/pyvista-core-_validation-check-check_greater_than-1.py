# Check if an array's values are greater than 0.
#
from pyvista import _validation
_validation.check_greater_than([1, 2, 3], value=0)
