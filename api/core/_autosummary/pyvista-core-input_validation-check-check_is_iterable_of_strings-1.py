# Check if a ``tuple`` only has ``str`` elements.
#
import pyvista.core.input_validation as valid
valid.check_is_iterable_of_strings(("cat", "dog"))
