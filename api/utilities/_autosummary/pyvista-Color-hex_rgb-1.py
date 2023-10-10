# Create a blue color with half opacity.
#
import pyvista as pv
c = pv.Color("blue", default_opacity="#80")
c
# Expected:
## Color(name='blue', hex='#0000ff80', opacity=128)
c.hex_rgb
# Expected:
## '#0000ff'
#
# Create a red color using an RGB hexadecimal value.
#
c = pv.Color("0xff0000")
c
# Expected:
## Color(name='red', hex='#ff0000ff', opacity=255)
c.hex_rgb
# Expected:
## '#ff0000'
