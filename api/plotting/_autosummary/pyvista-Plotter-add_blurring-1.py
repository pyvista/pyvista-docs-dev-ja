# Add two blurring passes to the plotter and show it.
#
import pyvista as pv
pl = pv.Plotter()
_ = pl.add_mesh(pv.Sphere(), show_edges=True)
pl.add_blurring()
pl.add_blurring()
pl.show()
