# Check if ``int`` is a subtype of ``np.integer``.
#
import numpy as np
import pyvista.core.input_validation as valid
valid.check_is_subdtype(float, np.floating)
#
# Check from multiple allowable dtypes.
#
valid.check_is_subdtype(int, [np.integer, np.floating])
#
# Check an array's dtype.
#
arr = np.array([1, 2, 3], dtype='uint8')
valid.check_is_subdtype(arr, np.integer)
