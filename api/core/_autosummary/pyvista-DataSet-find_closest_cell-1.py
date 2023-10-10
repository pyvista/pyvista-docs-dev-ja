# Find nearest cell on a sphere centered on the
# origin to the point ``[0.1, 0.2, 0.3]``.
#
import pyvista as pv
mesh = pv.Sphere()
point = [0.1, 0.2, 0.3]
index = mesh.find_closest_cell(point)
index
# Expected:
## 338
#
# Make sure that this cell indeed is the closest to
# ``[0.1, 0.2, 0.3]``.
#
import numpy as np
cell_centers = mesh.cell_centers()
relative_position = cell_centers.points - point
distance = np.linalg.norm(relative_position, axis=1)
np.argmin(distance)
# Expected:
## 338
#
# Find the nearest cells to several random points that
# are centered on the origin.
#
points = 2 * np.random.random((5000, 3)) - 1
indices = mesh.find_closest_cell(points)
indices.shape
# Expected:
## (5000,)
#
# For the closest cell, find the point inside the cell that is
# closest to the supplied point.  The rectangle is a unit square
# with 1 cell and 4 nodal points at the corners in the plane with
# ``z`` normal and ``z=0``.  The closest point inside the cell is
# not usually at a nodal point.
#
unit_square = pv.Rectangle()
index, closest_point = unit_square.find_closest_cell(
    [0.25, 0.25, 0.5], return_closest_point=True
)
closest_point
# Expected:
## array([0.25, 0.25, 0.  ])
#
# But, the closest point can be a nodal point, although the index of
# that point is not returned.  If the closest nodal point by index is
# desired, see :func:`DataSet.find_closest_point`.
#
index, closest_point = unit_square.find_closest_cell(
    [1.0, 1.0, 0.5], return_closest_point=True
)
closest_point
# Expected:
## array([1., 1., 0.])
