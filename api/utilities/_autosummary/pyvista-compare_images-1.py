# Compare two active plotters.
#
import pyvista as pv
pl1 = pv.Plotter()
_ = pl1.add_mesh(pv.Sphere(), smooth_shading=True)
pl2 = pv.Plotter()
_ = pl2.add_mesh(pv.Sphere(), smooth_shading=False)
error = pv.compare_images(pl1, pl2)
#
# Compare images from file.
#
import pyvista as pv
img1 = pv.read('img1.png')  # doctest:+SKIP
img2 = pv.read('img2.png')  # doctest:+SKIP
pv.compare_images(img1, img2)  # doctest:+SKIP
