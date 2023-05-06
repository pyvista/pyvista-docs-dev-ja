# Set the diffuse color to blue.
#
import pyvista as pv
prop = pv.Property()
prop.diffuse_color = 'b'
prop.diffuse_color
# Expected:
## Color(name='blue', hex='#0000ffff', opacity=255)
#
# Visualize setting the diffuse color to white with ``diffuse = 0.5``
#
prop.diffuse = 0.5
prop.diffuse_color = 'w'
prop.plot()
