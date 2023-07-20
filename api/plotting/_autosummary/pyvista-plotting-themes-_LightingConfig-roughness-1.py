# Set the global roughness value used in physically based rendering to
# ``0.25``.
#
import pyvista as pv
pv.global_theme.lighting_params.roughness = 0.25
pv.global_theme.lighting_params.roughness
# Expected:
## 0.25
