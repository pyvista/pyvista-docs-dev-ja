# Add a numpy array of points to a mesh.
#
import numpy as np
import pyvista as pv
rng = np.random.default_rng(seed=0)
points = rng.random((10, 3))
pl = pv.Plotter()
actor = pl.add_points(
    points, render_points_as_spheres=True, point_size=100.0
)
pl.show()
#
# Plot using the ``'points_gaussian'`` style
#
points = rng.random((10, 3))
pl = pv.Plotter()
actor = pl.add_points(points, style='points_gaussian')
pl.show()
