# Check if an array's values are less than 0.
#
from pyvista import _validation
_validation.check_less_than([-1, -2, -3], value=0)
