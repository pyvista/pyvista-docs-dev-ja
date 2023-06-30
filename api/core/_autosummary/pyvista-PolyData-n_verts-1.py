# Create a simple mesh containing just two points and return the
# number of vertices. By default, when constructing a PolyData with points but no cells,
# vertices are automatically created, one per point.
#
import pyvista
mesh = pyvista.PolyData([[1.0, 0.0, 0.0], [1.0, 1.0, 1.0]])
mesh.n_points, mesh.n_verts
# Expected:
## (2, 2)
#
# If any other cells are specified, these vertices are not created.
#
import pyvista
mesh = pyvista.PolyData(
    [[1.0, 0.0, 0.0], [1.0, 1.0, 1.0]], lines=[2, 0, 1]
)
mesh.n_points, mesh.n_verts
# Expected:
## (2, 0)
