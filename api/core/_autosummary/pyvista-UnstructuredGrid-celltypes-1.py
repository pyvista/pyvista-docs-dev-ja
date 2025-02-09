# This mesh contains only linear hexahedral cells, type
# :attr:`pyvista.CellType.HEXAHEDRON`, which evaluates to 12.
#
import pyvista as pv
from pyvista import examples
hex_beam = examples.load_hexbeam()
hex_beam.celltypes
# Expected:
## array([12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
##        12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12,
##        12, 12, 12, 12, 12, 12], dtype=uint8)
