# Change the global default background color to white.
#
import pyvista as pv
pv.global_theme.color = 'white'
#
# Show edges by default.
#
pv.global_theme.show_edges = True
#
# Create a new theme from the default theme and apply it globally.
#
from pyvista.plotting.themes import DocumentTheme
my_theme = DocumentTheme()
my_theme.color = 'red'
my_theme.background = 'white'
pv.global_theme.load_theme(my_theme)
