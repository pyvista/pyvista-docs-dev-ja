# Check if an array has a length of 2 or 3.
#
from pyvista import _validation
_validation.check_length([1, 2], exact_length=[2, 3])
#
# Check if an array has a minimum length of 3.
#
_validation.check_length((1, 2, 3), min_length=3)
#
# Check if a multidimensional array has a maximum length of 2.
#
_validation.check_length([[1, 2, 3], [4, 5, 6]], max_length=2)
