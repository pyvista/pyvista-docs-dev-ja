# Create a point cloud polydata and return the vertex cells.
#
import pyvista as pv
import numpy as np
rng = np.random.default_rng(seed=0)
points = rng.random((5, 3))
pdata = pv.PolyData(points)
pdata.verts
# Expected:
## array([1, 0, 1, 1, 1, 2, 1, 3, 1, 4])
#
# Set vertex cells.  Note how the mesh plots both the surface
# mesh and the additional vertices in a single plot.
#
mesh = pv.Plane(i_resolution=3, j_resolution=3)
mesh.verts = np.vstack(
    (
        np.ones(mesh.n_points, dtype=np.int64),
        np.arange(mesh.n_points),
    )
).T
mesh.plot(
    color='lightblue',
    render_points_as_spheres=True,
    point_size=60,
)
#
# Vertex cells can also be set to a ``CellArray``. The following
# ``verts`` assignment is equivalent to the one above.
#
mesh.verts = pv.CellArray.from_regular_cells(
    np.arange(mesh.n_points).reshape((-1, 1))
)
