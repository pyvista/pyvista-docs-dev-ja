# Set both the position and view of the camera.
#
import pyvista as pv
pv.global_theme.camera = {
    'position': [1, 1, 1],
    'viewup': [0, 0, 1],
}
#
# Set the default position of the camera.
#
pv.global_theme.camera['position'] = [1, 1, 1]
#
# Set the default view of the camera.
#
pv.global_theme.camera['viewup'] = [0, 0, 1]
