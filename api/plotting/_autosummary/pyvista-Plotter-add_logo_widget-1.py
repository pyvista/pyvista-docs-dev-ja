# Add a logo widget to the scene.
#
import pyvista as pv
pl = pv.Plotter()
_ = pl.add_logo_widget()
_ = pl.add_mesh(pv.Sphere(), show_edges=True)
pl.show()
