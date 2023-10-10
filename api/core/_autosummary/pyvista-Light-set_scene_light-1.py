import pyvista as pv
light = pv.Light()
light.set_scene_light()
light.light_type
# Expected:
## <LightType.SCENE_LIGHT: 3>
