# Check if an object is an instance of ``complex``.
#
import pyvista.core.input_validation as valid
valid.check_is_instance(1 + 2j, complex)
#
# Check if an object is an instance of one of several types.
#
valid.check_is_instance("eggs", (int, str))
