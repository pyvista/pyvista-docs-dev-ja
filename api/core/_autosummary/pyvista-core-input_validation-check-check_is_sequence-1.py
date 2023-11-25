# Check if an object is a sequence.
#
import numpy as np
import pyvista.core.input_validation as valid
valid.check_is_sequence([1, 2, 3])
valid.check_is_sequence("A")
