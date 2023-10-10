# Create a plotter without any lights and then enable the
# default light kit.
#
import pyvista as pv
pl = pv.Plotter(lighting=None)
pl.enable_lightkit()
actor = pl.add_mesh(pv.Cube(), show_edges=True)
pl.show()
