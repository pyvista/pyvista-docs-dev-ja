# Create a mesh with one face and one line
#
import pyvista as pv
mesh = pv.PolyData(
    [(0.0, 0, 0), (1, 0, 0), (0, 1, 0)],
    faces=[3, 0, 1, 2],
    lines=[2, 0, 1],
)
mesh.n_cells, mesh.n_faces_strict
# Expected:
## (2, 1)
