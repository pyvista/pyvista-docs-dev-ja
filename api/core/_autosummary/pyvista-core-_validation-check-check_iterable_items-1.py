# Check if a ``tuple`` only has ``int`` or ``float`` elements.
#
from pyvista import _validation
_validation.check_iterable_items((1, 2, 3.0), (int, float))
#
# Check if a ``list`` only has ``list`` elements.
#
from pyvista import _validation
_validation.check_iterable_items([[1], [2], [3]], list)
