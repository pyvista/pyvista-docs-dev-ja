# Create an image of a grid.
#
import pyvista as pv
source = pv.ImageGridSource(
    extent=(0, 20, 0, 20, 0, 0),
    spacing=(1, 1, 1),
)
source.output.plot(cpos='xy')
