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
# Initialize from just vertices.
#
vertices = np.array(
    [[0, 0, 0], [1, 0, 0], [1, 0.5, 0], [0, 0.5, 0]]
)
mesh = pv.PolyData(vertices)
#
# Initialize from vertices and faces.
#
faces = np.hstack([[3, 0, 1, 2], [3, 0, 3, 2]])
mesh = pv.PolyData(vertices, faces)
#
# Initialize from vertices and lines.
#
lines = np.hstack([[2, 0, 1], [2, 1, 2]])
mesh = pv.PolyData(vertices, lines=lines)
#
# Initialize from vertices and triangle strips.
#
strips = np.hstack([[4, 0, 1, 3, 2]])
mesh = pv.PolyData(vertices, strips=strips)
#
# Initialize from a filename.
#
mesh = pv.PolyData(examples.antfile)
