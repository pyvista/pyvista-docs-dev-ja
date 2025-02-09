# Read a ``'.GRDECL'`` file.
#
import pyvista as pv
grid = pv.read('file.GRDECL')  # doctest:+SKIP
#
# Unused keywords contained in the file are stored in :attr:`pyvista.DataObject.user_dict`:
#
grid.user_dict  # doctest:+SKIP
# Expected:
## {"MAPUNITS": ..., "GRIDUNIT": ..., ...}
