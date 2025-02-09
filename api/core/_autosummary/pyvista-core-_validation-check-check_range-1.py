# Check if `an array's values are in the range ``[0, 1]``.
#
from pyvista import _validation
_validation.check_range([0, 0.5, 1], rng=[0, 1])
