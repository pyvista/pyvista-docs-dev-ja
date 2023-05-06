# Set global PBR parameters.
#
import pyvista as pv
pv.global_theme.lighting_params.interpolation = 'pbr'
pv.global_theme.lighting_params.metallic = 0.5
pv.global_theme.lighting_params.roughness = 0.25
