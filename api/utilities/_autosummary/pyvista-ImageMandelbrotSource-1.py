# Create an image of the Mandelbrot set.
#
import pyvista as pv
source = pv.ImageMandelbrotSource(
    whole_extent=(0, 200, 0, 200, 0, 0),
    maxiter=100,
)
source.output.plot(cpos='xy')
