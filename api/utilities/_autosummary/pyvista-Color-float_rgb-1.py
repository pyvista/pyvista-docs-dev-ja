# Create a blue color with custom opacity.
#
import pyvista as pv
c = pv.Color("blue", default_opacity=0.6)
c
# Expected:
## Color(name='blue', hex='#0000ff99', opacity=153)
c.float_rgb
# Expected:
## (0.0, 0.0, 1.0)
#
# Create a red color using a float RGB sequence.
#
c = pv.Color([1.0, 0.0, 0.0])
c
# Expected:
## Color(name='red', hex='#ff0000ff', opacity=255)
c.float_rgb
# Expected:
## (1.0, 0.0, 0.0)
