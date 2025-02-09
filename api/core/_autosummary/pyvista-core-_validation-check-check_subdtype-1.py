# Check if ``float`` is a subtype of ``np.floating``.
#
import numpy as np
from pyvista import _validation
_validation.check_subdtype(float, np.floating)
#
# Check from multiple allowable dtypes.
#
_validation.check_subdtype(int, [np.integer, np.floating])
#
# Check an array's dtype.
#
array = np.array([1, 2, 3], dtype='uint8')
_validation.check_subdtype(array, np.integer)
