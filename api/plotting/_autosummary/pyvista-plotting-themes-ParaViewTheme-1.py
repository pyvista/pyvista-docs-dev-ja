# Make the paraview-like theme the global default.
#
import pyvista as pv
from pyvista import themes
pv.set_plot_theme(themes.ParaViewTheme())
#
# Alternatively, set via a string.
#
pv.set_plot_theme('paraview')
