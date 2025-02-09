# Plot a simple sphere while showing its edges.
#
import pyvista as pv
mesh = pv.Sphere()
mesh.plot(show_edges=True)
#
# Plot a volume mesh. Color by distance from the center of the
# ImageData. Note ``volume=True`` is passed.
#
import numpy as np
grid = pv.ImageData(dimensions=(32, 32, 32), spacing=(0.5, 0.5, 0.5))
grid['data'] = np.linalg.norm(grid.center - grid.points, axis=1)
grid['data'] = np.abs(grid['data'] - grid['data'].max()) ** 3
grid.plot(volume=True)
