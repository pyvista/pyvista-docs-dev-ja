import pyvista as pv
import vtk
import numpy as np
#
# Create an empty grid.
#
grid = pv.RectilinearGrid()
#
# Initialize from a vtk.vtkRectilinearGrid object
#
vtkgrid = vtk.vtkRectilinearGrid()
grid = pv.RectilinearGrid(vtkgrid)
#
# Create from NumPy arrays.
#
xrng = np.arange(-10, 10, 2)
yrng = np.arange(-10, 10, 5)
zrng = np.arange(-10, 10, 1)
grid = pv.RectilinearGrid(xrng, yrng, zrng)
grid.plot(show_edges=True)
