# Create a simple point cloud of 10 points from a numpy array.
#
import numpy as np
import pyvista as pv
rng = np.random.default_rng()
points = rng.random((10, 3))
pset = pv.PointSet(points)
#
# Plot the pointset. Note: this casts to a :class:`pyvista.PolyData`
# internally when plotting.
#
pset.plot(point_size=10)
