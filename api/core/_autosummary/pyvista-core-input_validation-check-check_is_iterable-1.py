# Check if an object is iterable.
#
import numpy as np
import pyvista.core.input_validation as valid
valid.check_is_iterable([1, 2, 3])
valid.check_is_iterable(np.array((4, 5, 6)))
