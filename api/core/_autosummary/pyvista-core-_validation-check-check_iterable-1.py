# Check if an object is iterable.
#
import numpy as np
from pyvista import _validation
_validation.check_iterable([1, 2, 3])
_validation.check_iterable(np.array((4, 5, 6)))
