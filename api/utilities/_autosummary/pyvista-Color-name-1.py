# Create a dark blue color with half opacity.
#
import pyvista as pv
c = pv.Color('darkblue', default_opacity=0.5)
c
# Expected:
## Color(name='darkblue', hex='#00008b80', opacity=128)
#
# When creating a new ``Color``, the name may be delimited with a space,
# hyphen, underscore, or written as a single word.
#
c = pv.Color('dark blue', default_opacity=0.5)
#
# Upper-case letters are also supported.
#
c = pv.Color('DarkBlue', default_opacity=0.5)
#
# However, the name is always standardized as a single lower-case word.
#
c
# Expected:
## Color(name='darkblue', hex='#00008b80', opacity=128)
