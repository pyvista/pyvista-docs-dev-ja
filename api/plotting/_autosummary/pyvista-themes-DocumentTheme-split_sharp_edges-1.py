# Enable the splitting of sharp edges globally.
#
import pyvista
pyvista.global_theme.split_sharp_edges = True
pyvista.global_theme.split_sharp_edges
# Expected:
## True
#
# Disable the splitting of sharp edges globally.
#
import pyvista
pyvista.global_theme.split_sharp_edges = False
pyvista.global_theme.split_sharp_edges
# Expected:
## False
