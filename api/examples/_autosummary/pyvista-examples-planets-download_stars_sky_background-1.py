# Load the night sky image as a background image.
#
from pyvista import examples
import pyvista as pv
pl = pv.Plotter()
image_path = examples.planets.download_stars_sky_background(load=False)
pl.add_background_image(image_path)
pl.show()
#
# .. seealso::
#
#     :ref:`Stars Sky Background Dataset <stars_sky_background_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :func:`~pyvista.examples.planets.load_mars`
#         Load Mars as a textured sphere.
#
#     :ref:`Milkyway Sky Background Dataset <milkyway_sky_background_dataset>`
#         Sky texture of the Milky Way galaxy.
#
#     :ref:`planets_example`
