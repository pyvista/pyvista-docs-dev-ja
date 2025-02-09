# Check if an object is an instance of ``complex``.
#
from pyvista import _validation
_validation.check_instance(1 + 2j, complex)
#
# Check if an object is an instance of one of several types.
#
_validation.check_instance('eggs', (int, str))
