# Validate a one-dimensional array has at least length two, is
# monotonically increasing (i.e. has strict ascending order), and
# is within some range.
#
from pyvista import _validation
array_in = (1, 2, 3, 5, 8, 13)
rng = (0, 20)
_validation.validate_array(
    array_in,
    must_have_shape=(-1),
    must_have_min_length=2,
    must_be_sorted=dict(strict=True),
    must_be_in_range=rng,
)
# Expected:
## array([ 1,  2,  3,  5,  8, 13])
