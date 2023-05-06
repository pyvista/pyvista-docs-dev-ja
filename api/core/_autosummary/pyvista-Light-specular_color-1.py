# Create a light and set its specular color to bright green.
#
import pyvista as pv
light = pv.Light()
light.specular_color = '#00FF00'
light.specular_color
# Expected:
## Color(name='lime', hex='#00ff00ff', opacity=255)
