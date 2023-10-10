# Create a blue color with half opacity.
#
import pyvista as pv
c = pv.Color("blue", opacity=128)
c
# Expected:
## Color(name='blue', hex='#0000ff80', opacity=128)
c.int_rgba
# Expected:
## (0, 0, 255, 128)
#
# Create a transparent red color using an integer RGBA sequence.
#
c = pv.Color([255, 0, 0, 64])
c
# Expected:
## Color(name='red', hex='#ff000040', opacity=64)
c.int_rgba
# Expected:
## (255, 0, 0, 64)
