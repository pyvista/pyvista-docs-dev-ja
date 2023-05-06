# Enable the splitting of sharp edges globally.
#
import pyvista as pv
pv.global_theme.split_sharp_edges = True
pv.global_theme.split_sharp_edges
# Expected:
## True
#
# Disable the splitting of sharp edges globally.
#
import pyvista as pv
pv.global_theme.split_sharp_edges = False
pv.global_theme.split_sharp_edges
# Expected:
## False
