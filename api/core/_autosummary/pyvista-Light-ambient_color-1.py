# Create a light and set its ambient color to red.
#
import pyvista as pv
light = pv.Light()
light.ambient_color = 'red'
light.ambient_color
# Expected:
## Color(name='red', hex='#ff0000ff', opacity=255)
