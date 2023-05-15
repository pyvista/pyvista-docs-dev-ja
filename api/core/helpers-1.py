# Wrap a numpy array representing a random point cloud.
#
import numpy as np
import pyvista
points = np.random.random((10, 3))
cloud = pyvista.wrap(points)
cloud
# Expected:
## PolyData (...)
##   N Cells:    10
##   N Points:   10
##   N Strips:   0
##   X Bounds:   ...
##   Y Bounds:   ...
##   Z Bounds:   ...
##   N Arrays:   0
#
# Wrap a VTK object.
#
import pyvista
import vtk
points = vtk.vtkPoints()
p = [1.0, 2.0, 3.0]
vertices = vtk.vtkCellArray()
pid = points.InsertNextPoint(p)
_ = vertices.InsertNextCell(1)
_ = vertices.InsertCellPoint(pid)
point = vtk.vtkPolyData()
_ = point.SetPoints(points)
_ = point.SetVerts(vertices)
mesh = pyvista.wrap(point)
mesh
# Expected:
## PolyData (...)
##   N Cells:    1
##   N Points:   1
##   N Strips:   0
##   X Bounds:   1.000e+00, 1.000e+00
##   Y Bounds:   2.000e+00, 2.000e+00
##   Z Bounds:   3.000e+00, 3.000e+00
##   N Arrays:   0
#
# Wrap a Trimesh object.
#
import trimesh
import pyvista
points = [[0, 0, 0], [0, 0, 1], [0, 1, 0]]
faces = [[0, 1, 2]]
tmesh = trimesh.Trimesh(points, faces=faces, process=False)
mesh = pyvista.wrap(tmesh)
mesh  # doctest:+SKIP
# Expected:
## PolyData (0x7fc55ff27ad0)
##   N Cells:  1
##   N Points: 3
##   X Bounds: 0.000e+00, 0.000e+00
##   Y Bounds: 0.000e+00, 1.000e+00
##   Z Bounds: 0.000e+00, 1.000e+00
##   N Arrays: 0
