import pyvista as pv
import vtk
import numpy as np
#
# Create an empty structured grid.
#
grid = pv.StructuredGrid()
#
# Initialize from a ``vtk.vtkStructuredGrid`` object
#
vtkgrid = vtk.vtkStructuredGrid()
grid = pv.StructuredGrid(vtkgrid)
#
# Create from NumPy arrays.
#
xrng = np.arange(-10, 10, 2, dtype=np.float32)
yrng = np.arange(-10, 10, 5, dtype=np.float32)
zrng = np.arange(-10, 10, 1, dtype=np.float32)
x, y, z = np.meshgrid(xrng, yrng, zrng, indexing='ij')
grid = pv.StructuredGrid(x, y, z)
grid
# Expected:
## StructuredGrid (...)
##   N Cells:      513
##   N Points:     800
##   X Bounds:     -1.000e+01, 8.000e+00
##   Y Bounds:     -1.000e+01, 5.000e+00
##   Z Bounds:     -1.000e+01, 9.000e+00
##   Dimensions:   10, 4, 20
##   N Arrays:     0
