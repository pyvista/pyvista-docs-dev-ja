# Load an image with point data.
#
from pyvista import examples
image = examples.load_uniform()
#
# Show the current properties and point arrays of the image.
#
image
# Expected:
## ImageData (...)
##   N Cells:      729
##   N Points:     1000
##   X Bounds:     0.000e+00, 9.000e+00
##   Y Bounds:     0.000e+00, 9.000e+00
##   Z Bounds:     0.000e+00, 9.000e+00
##   Dimensions:   10, 10, 10
##   Spacing:      1.000e+00, 1.000e+00, 1.000e+00
##   N Arrays:     2
#
image.point_data.keys()
# Expected:
## ['Spatial Point Data']
#
# Re-mesh the points and point data as cells and cell data.
#
cells_image = image.points_to_cells()
#
# Show the properties and cell arrays of the re-meshed image.
#
cells_image
# Expected:
## ImageData (...)
##   N Cells:      1000
##   N Points:     1331
##   X Bounds:     -5.000e-01, 9.500e+00
##   Y Bounds:     -5.000e-01, 9.500e+00
##   Z Bounds:     -5.000e-01, 9.500e+00
##   Dimensions:   11, 11, 11
##   Spacing:      1.000e+00, 1.000e+00, 1.000e+00
##   N Arrays:     1
#
cells_image.cell_data.keys()
# Expected:
## ['Spatial Point Data']
#
# Observe that:
#
# - The input point array is now a cell array
# - The output has one less array (the input cell data is ignored)
# - The dimensions have increased by one
# - The bounds have increased by half the spacing
# - The output ``N Cells`` equals the input ``N Points``
#
# Since the input points are 3D (i.e. there are no singleton dimensions), the
# output cells are 3D :attr:`~pyvista.CellType.VOXEL` cells.
#
cells_image.get_cell(0).type
# Expected:
## <CellType.VOXEL: 11>
#
# If the input points are 2D (i.e. one dimension is singleton), the
# output cells are 2D :attr:`~pyvista.CellType.PIXEL` cells when ``dimensions`` is
# set to ``'preserve'``.
#
image2D = examples.download_beach()
image2D.dimensions
# Expected:
## (100, 100, 1)
#
pixel_cells_image = image2D.points_to_cells(dimensionality='preserve')
pixel_cells_image.dimensions
# Expected:
## (101, 101, 1)
pixel_cells_image.get_cell(0).type
# Expected:
## <CellType.PIXEL: 8>
#
# This is equivalent as requesting a 2D output.
#
pixel_cells_image = image2D.points_to_cells(dimensionality='2D')
pixel_cells_image.dimensions
# Expected:
## (101, 101, 1)
pixel_cells_image.get_cell(0).type
# Expected:
## <CellType.PIXEL: 8>
#
# Use ``(True, True, True)`` to re-mesh 2D points as 3D cells.
#
voxel_cells_image = image2D.points_to_cells(
    dimensionality=(True, True, True)
)
voxel_cells_image.dimensions
# Expected:
## (101, 101, 2)
voxel_cells_image.get_cell(0).type
# Expected:
## <CellType.VOXEL: 11>
#
# Or request a 3D output.
#
voxel_cells_image = image2D.points_to_cells(dimensionality='3D')
voxel_cells_image.dimensions
# Expected:
## (101, 101, 2)
voxel_cells_image.get_cell(0).type
# Expected:
## <CellType.VOXEL: 11>
