# Create banded contour and fill.
#
import pyvista as pv
from pyvista import examples
image = examples.download_st_helens()
contours = image.contour([1302.3334, 1922.6666])
filled = contours.triangulate_contours()
#
pl = pv.Plotter(shape=(1, 2))
_ = pl.add_mesh(image, show_scalar_bar=False)
_ = pl.add_mesh(contours, color='black')
pl.subplot(0, 1)
_ = pl.add_mesh(contours, color='black')
_ = pl.add_mesh(filled, color='red')
pl.link_views()
pl.view_xy()
pl.show()
