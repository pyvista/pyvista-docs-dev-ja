# Create a light and set its diffuse color to blue.
#
import pyvista as pv
light = pv.Light()
light.diffuse_color = (0.0, 0.0, 1.0)
light.diffuse_color
# Expected:
## Color(name='blue', hex='#0000ffff', opacity=255)
