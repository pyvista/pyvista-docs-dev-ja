# Create a custom theme from the default theme and load it into
# the global theme of pyvista.
#
import pyvista as pv
from pyvista.plotting.themes import DocumentTheme
my_theme = DocumentTheme()
my_theme.font.size = 20
my_theme.font.title_size = 40
my_theme.cmap = 'jet'
pv.global_theme.load_theme(my_theme)
pv.global_theme.font.size
# Expected:
## 20
#
# Create a custom theme from the dark theme and load it into
# pv.
#
from pyvista.plotting.themes import DarkTheme
my_theme = DarkTheme()
my_theme.show_edges = True
pv.global_theme.load_theme(my_theme)
pv.global_theme.show_edges
# Expected:
## True
