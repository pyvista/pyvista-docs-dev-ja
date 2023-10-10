# Create a blue color with half opacity.
#
import pyvista as pv
c = pv.Color("blue", default_opacity="#80")
c
# Expected:
## Color(name='blue', hex='#0000ff80', opacity=128)
c.hex_rgba
# Expected:
## '#0000ff80'
#
# Create a transparent red color using an RGBA hexadecimal value.
#
c = pv.Color("0xff000040")
c
# Expected:
## Color(name='red', hex='#ff000040', opacity=64)
c.hex_rgba
# Expected:
## '#ff000040'
