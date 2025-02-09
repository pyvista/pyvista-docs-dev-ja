# Construct a pyramid from five points and five faces
#
import pyvista as pv
points = [
    (1, 1, 0),
    (-1, 1, 0),
    (-1, -1, 0),
    (1, -1, 0),
    (0, 0, 1.61),
]
faces = [
    (0, 1, 2, 3),
    (0, 3, 4),
    (0, 4, 1),
    (3, 2, 4),
    (2, 1, 4),
]
pyramid = pv.PolyData.from_irregular_faces(points, faces)
pyramid.plot()
