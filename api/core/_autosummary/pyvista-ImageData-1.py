# Create an empty ImageData.
#
import pyvista as pv
grid = pv.ImageData()
#
# Initialize from a ``vtk.vtkImageData`` object.
#
import vtk
vtkgrid = vtk.vtkImageData()
grid = pv.ImageData(vtkgrid)
#
# Initialize using just the grid dimensions and default
# spacing and origin. These must be keyword arguments.
#
grid = pv.ImageData(dimensions=(10, 10, 10))
#
# Initialize using dimensions and spacing.
#
grid = pv.ImageData(
    dimensions=(10, 10, 10),
    spacing=(2, 1, 5),
)
#
# Initialize using dimensions, spacing, and an origin.
#
grid = pv.ImageData(
    dimensions=(10, 10, 10),
    spacing=(2, 1, 5),
    origin=(10, 35, 50),
)
#
# Initialize from another ImageData.
#
grid = pv.ImageData(
    dimensions=(10, 10, 10),
    spacing=(2, 1, 5),
    origin=(10, 35, 50),
)
grid_from_grid = pv.ImageData(grid)
grid_from_grid == grid
# Expected:
## True
