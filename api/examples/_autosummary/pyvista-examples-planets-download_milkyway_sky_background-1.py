# Load the Milky Way sky image as a background image.
#
from pyvista import examples
import pyvista as pv
pl = pv.Plotter()
image_path = examples.planets.download_milkyway_sky_background(load=False)
pl.add_background_image(image_path)
pl.show()
#
# .. seealso::
#
#     :ref:`Milkyway Sky Background Dataset <milkyway_sky_background_dataset>`
#         See this dataset in the Dataset Gallery for more info.
#
#     :ref:`Stars Sky Background Dataset <stars_sky_background_dataset>`
#         Night sky stars texture.
#
#     :ref:`planets_example`
