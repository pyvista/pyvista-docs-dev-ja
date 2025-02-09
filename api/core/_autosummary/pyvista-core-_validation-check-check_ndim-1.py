# Check if an array is one-dimensional
#
import numpy as np
from pyvista import _validation
_validation.check_ndim([1, 2, 3], ndim=1)
#
# Check if an array is two-dimensional or a scalar.
#
_validation.check_ndim(1, ndim=(0, 2))
