# Construct a Kochanek spline.
#
import numpy as np
import pyvista as pv
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
points = np.column_stack((x, y, z))
kochanek_spline = pv.KochanekSpline(points, n_points=6)
kochanek_spline.plot(line_width=4, color='k')
