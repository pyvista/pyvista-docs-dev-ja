# Globally enable emissive lighting when using the point Gaussian style.
#
import pyvista as pv
pv.global_theme.lighting_params.emissive = True
pv.global_theme.lighting_params.emissive
# Expected:
## True
