# Construct a tetrahedron from four triangles
#
import pyvista as pv
points = [[1.0, 1, 1], [-1, 1, -1], [1, -1, -1], [-1, -1, 1]]
faces = [[0, 1, 2], [1, 3, 2], [0, 2, 3], [0, 3, 1]]
tetra = pv.PolyData.from_regular_faces(points, faces)
