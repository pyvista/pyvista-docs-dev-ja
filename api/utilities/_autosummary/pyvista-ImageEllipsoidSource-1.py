# Create an image of an ellipsoid.
#
import pyvista as pv
source = pv.ImageEllipsoidSource(
    whole_extent=(0, 20, 0, 20, 0, 0),
    center=(10, 10, 0),
    radius=(3, 4, 5),
)
source.output.plot(cpos='xy')
