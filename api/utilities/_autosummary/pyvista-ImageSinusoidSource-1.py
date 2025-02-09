# Create an image of a sinusoid.
#
import pyvista as pv
source = pv.ImageSinusoidSource(
    whole_extent=(0, 200, 0, 200, 0, 0),
    period=20.0,
    phase=0.0,
    amplitude=255,
    direction=(1.0, 0.0, 0.0),
)
source.output.plot(cpos='xy')
