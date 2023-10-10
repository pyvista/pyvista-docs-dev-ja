# This mesh contains only linear hexahedral cells, type
# ``CellType.HEXAHEDRON``, which evaluates to 12.
#
import pyvista as pv
from pyvista import examples
hex_beam = pv.read(examples.hexbeamfile)
hex_beam.celltypes  # doctest:+SKIP
# Expected:
## array([12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
##        12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
##        12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12],
##        dtype=uint8)
