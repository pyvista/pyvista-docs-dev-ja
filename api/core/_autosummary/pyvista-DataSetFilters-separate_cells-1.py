# Load the example hex beam and separate its cells. This increases the
# total number of points in the dataset since points are no longer
# shared.
#
from pyvista import examples
grid = examples.load_hexbeam()
grid.n_points
# Expected:
## 99
sep_grid = grid.separate_cells()
sep_grid.n_points
# Expected:
## 320
#
# See the :ref:`point_cell_scalars_example` for a more detailed example
