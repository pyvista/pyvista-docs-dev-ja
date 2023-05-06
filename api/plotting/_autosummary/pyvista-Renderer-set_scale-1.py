# Set the scale in the z direction to be 2 times that of
# nominal.  Leave the other axes unscaled.
#
import pyvista
pl = pyvista.Plotter()
pl.set_scale(zscale=2)
_ = pl.add_mesh(pyvista.Sphere())  # perfect sphere
pl.show()
