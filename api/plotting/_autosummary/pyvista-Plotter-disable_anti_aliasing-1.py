import pyvista as pv
pl = pv.Plotter()
pl.disable_anti_aliasing()
_ = pl.add_mesh(pv.Sphere(), show_edges=True)
pl.show()
#
# See :ref:`anti_aliasing_example` for a full example demonstrating
