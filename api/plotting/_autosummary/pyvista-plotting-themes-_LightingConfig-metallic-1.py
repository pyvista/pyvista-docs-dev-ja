# Set the global metallic value used in physically based rendering to
# ``0.5``.
#
import pyvista as pv
pv.global_theme.lighting_params.metallic = 0.5
pv.global_theme.lighting_params.metallic
# Expected:
## 0.5
