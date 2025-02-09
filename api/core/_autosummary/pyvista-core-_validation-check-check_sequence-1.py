# Check if an object is a sequence.
#
import numpy as np
from pyvista import _validation
_validation.check_sequence([1, 2, 3])
_validation.check_sequence('A')
