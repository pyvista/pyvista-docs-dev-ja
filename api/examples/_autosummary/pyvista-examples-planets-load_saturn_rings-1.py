import pyvista as pv
from pyvista import examples
pl = pv.Plotter()
image_path = examples.planets.download_stars_sky_background(
    load=False
)
pl.add_background_image(image_path)
_ = pl.add_mesh(examples.planets.load_saturn_rings())
pl.show()
