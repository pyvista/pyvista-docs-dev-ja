# Get the 0-th cell.
#
from pyvista import examples
mesh = examples.load_airplane()
cell = mesh.get_cell(0)
cell
# Expected:
## Cell ...
#
# Get the point ids of the first cell
#
cell.point_ids
# Expected:
## [0, 1, 2]
#
# Get the point coordinates of the first cell
#
cell.points
# Expected:
## array([[897.0,  48.8,  82.3],
##        [906.6,  48.8,  80.7],
##        [907.5,  55.5,  83.7]])
#
# For the first cell, get the points associated with the first edge
#
cell.edges[0].point_ids
# Expected:
## [0, 1]
#
# For a Tetrahedron, get the point ids of the last face
#
mesh = examples.cells.Tetrahedron()
cell = mesh.get_cell(0)
cell.faces[-1].point_ids
# Expected:
## [0, 2, 1]
