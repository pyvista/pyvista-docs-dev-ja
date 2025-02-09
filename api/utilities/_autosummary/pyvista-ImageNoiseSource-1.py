# Create an image of noise.
#
import pyvista as pv
source = pv.ImageNoiseSource(
    whole_extent=(0, 200, 0, 200, 0, 0),
    minimum=0,
    maximum=255,
    seed=0,
)
source.output.plot(cpos='xy')
