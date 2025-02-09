# Use the axes orientation widget instead of the default arrows.
#
import pyvista as pv
pl = pv.Plotter()
_ = pl.add_mesh(pv.Sphere())
_ = pl.add_box_axes()
pl.show()
