# Load the night sky image as a background image.
#
from pyvista import examples
import pyvista as pv
pl = pv.Plotter()
image_path = examples.planets.download_stars_sky_background(
    load=False
)
pl.add_background_image(image_path)
pl.show()
