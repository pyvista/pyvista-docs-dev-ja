import pyvista as pv
pv.global_theme.lighting_params.interpolation = 'Phong'
pv.global_theme.lighting_params.interpolation
# Expected:
## <InterpolationType.PHONG: 2>
