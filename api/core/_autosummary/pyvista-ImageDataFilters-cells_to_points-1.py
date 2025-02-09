# Load an image with cell data.
#
from pyvista import examples
image = examples.load_uniform()
#
# Show the current properties and cell arrays of the image.
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
image.cell_data.keys()
# Expected:
## ['Spatial Cell Data']
#
# Re-mesh the cells and cell data as points and point data.
#
points_image = image.cells_to_points()
#
# Show the properties and point arrays of the re-meshed image.
#
points_image
# Expected:
## ImageData (...)
##   N Cells:      512
##   N Points:     729
##   X Bounds:     5.000e-01, 8.500e+00
##   Y Bounds:     5.000e-01, 8.500e+00
##   Z Bounds:     5.000e-01, 8.500e+00
##   Dimensions:   9, 9, 9
##   Spacing:      1.000e+00, 1.000e+00, 1.000e+00
##   N Arrays:     1
#
points_image.point_data.keys()
# Expected:
## ['Spatial Cell Data']
#
# Observe that:
#
# - The input cell array is now a point array
# - The output has one less array (the input point data is ignored)
# - The dimensions have decreased by one
# - The bounds have decreased by half the spacing
# - The output ``N Points`` equals the input ``N Cells``
