# Create a blue color with half opacity.
#
import pyvista as pv
c = pv.Color("blue", opacity=128)
c
# Expected:
## Color(name='blue', hex='#0000ff80', opacity=128)
c.int_rgb
# Expected:
## (0, 0, 255)
#
# Create a red color using an integer RGB sequence.
#
c = pv.Color([255, 0, 0])
c
# Expected:
## Color(name='red', hex='#ff0000ff', opacity=255)
c.int_rgb
# Expected:
## (255, 0, 0)
