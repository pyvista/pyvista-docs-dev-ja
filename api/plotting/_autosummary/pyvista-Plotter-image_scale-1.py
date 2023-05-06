# Double the resolution of a screenshot.
#
import pyvista as pv
pl = pv.Plotter()
_ = pl.add_mesh(pv.Sphere())
pl.image_scale = 2
pl.screenshot('screenshot.png')  # doctest:+SKIP
#
# Set the image scale from ``Plotter``.
#
import pyvista as pv
pl = pv.Plotter(image_scale=2)
_ = pl.add_mesh(pv.Sphere())
pl.screenshot('screenshot.png')  # doctest:+SKIP
