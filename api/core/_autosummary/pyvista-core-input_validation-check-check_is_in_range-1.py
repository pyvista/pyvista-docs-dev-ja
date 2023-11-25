# Check if `an array's values are in the range ``[0, 1]``.
#
import pyvista.core.input_validation as valid
valid.check_is_in_range([0, 0.5, 1], rng=[0, 1])
