# Create an empty UniformGrid.
#
import pyvista
grid = pyvista.UniformGrid()
#
# Initialize from a ``vtk.vtkImageData`` object.
#
import vtk
vtkgrid = vtk.vtkImageData()
grid = pyvista.UniformGrid(vtkgrid)
#
# Initialize using just the grid dimensions and default
# spacing and origin. These must be keyword arguments.
#
grid = pyvista.UniformGrid(dimensions=(10, 10, 10))
#
# Initialize using dimensions and spacing.
#
grid = pyvista.UniformGrid(
    dimensions=(10, 10, 10),
    spacing=(2, 1, 5),
)
#
# Initialize using dimensions, spacing, and an origin.
#
grid = pyvista.UniformGrid(
    dimensions=(10, 10, 10),
    spacing=(2, 1, 5),
    origin=(10, 35, 50),
)
#
# Initialize from another UniformGrid.
#
grid = pyvista.UniformGrid(
    dimensions=(10, 10, 10),
    spacing=(2, 1, 5),
    origin=(10, 35, 50),
)
grid_from_grid = pyvista.UniformGrid(grid)
grid_from_grid == grid
# Expected:
## True
