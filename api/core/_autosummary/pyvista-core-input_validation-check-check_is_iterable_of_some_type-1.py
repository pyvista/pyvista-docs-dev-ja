# Check if a ``tuple`` only has ``int`` or ``float`` elements.
#
import pyvista.core.input_validation as valid
valid.check_is_iterable_of_some_type((1, 2, 3.0), (int, float))
#
# Check if a ``list`` only has ``list`` elements.
#
import pyvista.core.input_validation as valid
valid.check_is_iterable_of_some_type([[1], [2], [3]], list)
