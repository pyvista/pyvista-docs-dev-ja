# Enable super-sample anti-aliasing (SSAA).
#
import pyvista as pv
pl = pv.Plotter()
pl.enable_anti_aliasing('ssaa')
_ = pl.add_mesh(pv.Sphere(), show_edges=True)
pl.show()
#
# See :ref:`anti_aliasing_example` for a full example demonstrating
