import vtk
import numpy as np
from pyvista import examples
import pyvista as pv
#
# Create an empty mesh.
#
mesh = pv.PolyData()
#
# Initialize from a ``vtk.vtkPolyData`` object.
#
vtkobj = vtk.vtkPolyData()
mesh = pv.PolyData(vtkobj)
#
# Initialize from just points, creating vertices
#
points = np.array([[0, 0, 0], [1, 0, 0], [1, 0.5, 0], [0, 0.5, 0]])
mesh = pv.PolyData(points)
#
# Initialize from points and faces, creating polygonal faces.
#
faces = np.hstack([[3, 0, 1, 2], [3, 0, 3, 2]])
mesh = pv.PolyData(points, faces)
#
# Initialize from points and lines.
#
lines = np.hstack([[2, 0, 1], [2, 1, 2]])
mesh = pv.PolyData(points, lines=lines)
#
# Initialize from points and triangle strips.
#
strips = np.hstack([[4, 0, 1, 3, 2]])
mesh = pv.PolyData(points, strips=strips)
#
# It is also possible to create with multiple cell types.
#
verts = [1, 0]
lines = [2, 1, 2]
mesh = pv.PolyData(points, verts=verts, lines=lines)
#
# Initialize from a filename.
#
mesh = pv.PolyData(examples.antfile)
