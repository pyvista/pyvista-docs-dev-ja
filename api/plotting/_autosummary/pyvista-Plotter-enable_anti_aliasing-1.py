# Enable super-sample anti-aliasing (SSAA).
#
import pyvista
pl = pyvista.Plotter()
pl.enable_anti_aliasing('ssaa')
_ = pl.add_mesh(pyvista.Sphere(), show_edges=True)
pl.show()
#
# See :ref:`anti_aliasing_example` for a full example demonstrating
