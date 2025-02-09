# Create an image of Gaussian pixel values.
#
import pyvista as pv
source = pv.ImageGaussianSource(
    center=(100, 100, 0),
    whole_extent=(0, 200, 0, 200, 0, 0),
    maximum=255,
    std=100.0,
)
source.output.plot(cpos='xy')
