import numpy as np
import pyvista as pv

rng = np.random.default_rng(seed=0)
points = rng.random((100, 3))
mesh = pv.PolyData(points)
mesh.plot(point_size=10, style='points')