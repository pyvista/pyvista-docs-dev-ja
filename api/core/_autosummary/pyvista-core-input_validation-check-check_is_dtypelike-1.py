# Check if an input is dtype-like.
#
import numpy as np
import pyvista.core.input_validation as valid
valid.check_is_dtypelike(float)
valid.check_is_dtypelike(np.dtype(np.integer))
valid.check_is_dtypelike('uint8')
