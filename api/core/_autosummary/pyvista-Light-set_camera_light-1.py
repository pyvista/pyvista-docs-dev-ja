import pyvista as pv
light = pv.Light()
light.set_camera_light()
light.light_type
# Expected:
## <LightType.CAMERA_LIGHT: 2>
