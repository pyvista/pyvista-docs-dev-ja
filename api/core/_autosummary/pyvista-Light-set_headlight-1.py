import pyvista as pv
light = pv.Light()
light.set_headlight()
light.light_type
# Expected:
## <LightType.HEADLIGHT: 1>
