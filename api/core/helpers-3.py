import numpy as np
import pyvista as pv
points = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0]])
poly = pv.lines_from_points(points)
poly.plot(line_width=5)
