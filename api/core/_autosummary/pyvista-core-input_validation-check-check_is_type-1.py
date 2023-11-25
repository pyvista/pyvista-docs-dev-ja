# Check if an object is type ``dict`` or ``set``.
#
import pyvista.core.input_validation as valid
valid.check_is_type({'spam': "eggs"}, (dict, set))
