# Set the ambient color to blue.
#
import pyvista as pv
prop = pv.Property()
prop.ambient_color = 'b'
prop.ambient_color
# Expected:
## Color(name='blue', hex='#0000ffff', opacity=255)
#
# Visualize setting the ambient color to blue with ``ambient = 0.1``
#
prop.ambient = 0.1
prop.ambient_color = 'b'
prop.plot()
