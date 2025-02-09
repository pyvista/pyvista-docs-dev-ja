# Check if an object is type ``dict`` or ``set``.
#
from pyvista import _validation
_validation.check_type({'spam': 'eggs'}, (dict, set))
