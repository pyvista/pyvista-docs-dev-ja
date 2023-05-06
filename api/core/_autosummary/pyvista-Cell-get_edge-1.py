# Extract a single edge from a face and output the IDs of the edge
# points.
#
import pyvista
mesh = pyvista.Sphere()
cell = mesh.get_cell(0)
edge = cell.get_edge(0)
edge.point_ids
# Expected:
## [2, 30]
