# Enable plotting of empty meshes.
#
import pyvista as pv
pv.global_theme.allow_empty_mesh = True
#
# Now add an empty mesh to a plotter
#
pl = pv.Plotter()
_ = pl.add_mesh(pv.PolyData())
pl.show()  # doctest: +SKIP
