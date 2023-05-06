# Show the Default zoom.
#
import pyvista as pv
pl = pv.Plotter()
_ = pl.add_mesh(pv.Sphere())
pl.camera.zoom(1.0)
pl.show()
#
# Show 2x zoom.
#
pl = pv.Plotter()
_ = pl.add_mesh(pv.Sphere())
pl.camera.zoom(2.0)
pl.show()
#
# Zoom so the actor fills the entire render window.
#
pl = pv.Plotter()
_ = pl.add_mesh(pv.Sphere())
pl.camera.zoom('tight')
pl.show()
