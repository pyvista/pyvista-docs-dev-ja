# Set the specular color to blue.
#
import pyvista as pv
prop = pv.Property()
prop.specular_color = 'b'
prop.specular_color
# Expected:
## Color(name='blue', hex='#0000ffff', opacity=255)
#
# Visualize setting the specular color to blue with ``specular = 0.2``
#
prop.specular = 0.2
prop.specular_color = 'r'
prop.plot()
