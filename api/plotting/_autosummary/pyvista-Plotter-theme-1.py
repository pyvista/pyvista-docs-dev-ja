# Use the dark theme for a plotter.
#
import pyvista as pv
from pyvista import themes
pl = pv.Plotter()
pl.theme = themes.DarkTheme()
actor = pl.add_mesh(pv.Sphere())
pl.show()
