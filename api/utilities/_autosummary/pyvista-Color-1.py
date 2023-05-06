# Create a transparent green color using a color name, float RGBA sequence,
# integer RGBA sequence and RGBA hexadecimal string.
#
import pyvista
pyvista.Color("green", opacity=0.5)
# Expected:
## Color(name='green', hex='#00800080', opacity=128)
pyvista.Color([0.0, 0.5, 0.0, 0.5])
# Expected:
## Color(name='green', hex='#00800080', opacity=128)
pyvista.Color([0, 128, 0, 128])
# Expected:
## Color(name='green', hex='#00800080', opacity=128)
pyvista.Color("#00800080")
# Expected:
## Color(name='green', hex='#00800080', opacity=128)
