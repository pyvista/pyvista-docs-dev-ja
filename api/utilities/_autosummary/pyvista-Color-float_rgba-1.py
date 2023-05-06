# Create a blue color with custom opacity.
#
import pyvista
c = pyvista.Color("blue", opacity=0.6)
c
# Expected:
## Color(name='blue', hex='#0000ff99', opacity=153)
c.float_rgba
# Expected:
## (0.0, 0.0, 1.0, 0.6)
#
# Create a transparent red color using a float RGBA sequence.
#
c = pyvista.Color([1.0, 0.0, 0.0, 0.2])
c
# Expected:
## Color(name='red', hex='#ff000033', opacity=51)
c.float_rgba
# Expected:
## (1.0, 0.0, 0.0, 0.2)
