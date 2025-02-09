# Check if ``"A"`` is in a list of strings.
#
from pyvista import _validation
_validation.check_contains(['A', 'B', 'C'], must_contain='A')
