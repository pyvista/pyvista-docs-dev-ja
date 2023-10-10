# Integrate data on a sphere mesh.
#
import pyvista as pv
import numpy as np
sphere = pv.Sphere(theta_resolution=100, phi_resolution=100)
sphere.point_data["data"] = 2 * np.ones(sphere.n_points)
integrated = sphere.integrate_data()
#
# There is only 1 point and cell, so access the only value.
#
integrated["Area"][0]
# Expected:
## 3.14
integrated["data"][0]
# Expected:
## 6.28
