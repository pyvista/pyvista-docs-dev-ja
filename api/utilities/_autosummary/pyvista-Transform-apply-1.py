# Apply a transformation to a point.
#
import numpy as np
import pyvista as pv
point = (1, 2, 3)
transform = pv.Transform().scale(2)
transformed_point = transform.apply(point)
transformed_point
# Expected:
## array([2., 4., 6.])
#
# Apply a transformation to a points array.
#
points = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
transformed_points = transform.apply(points)
transformed_points
# Expected:
## array([[ 2.,  4.,  6.],
##        [ 8., 10., 12.]])
#
# Apply a transformation to a dataset.
#
dataset = pv.PolyData(points)
transformed_dataset = transform.apply(dataset)
transformed_dataset.points
# Expected:
## pyvista_ndarray([[ 2.,  4.,  6.],
##                  [ 8., 10., 12.]])
#
# Apply the inverse.
#
inverted_dataset = transform.apply(dataset, inverse=True)
inverted_dataset.points
# Expected:
## pyvista_ndarray([[0.5, 1. , 1.5],
##                  [2. , 2.5, 3. ]])
