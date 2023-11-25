# Check if an object is scalar.
#
import numpy as np
import pyvista.core.input_validation as valid
valid.check_is_scalar(0.0)
valid.check_is_scalar(np.array(1))
